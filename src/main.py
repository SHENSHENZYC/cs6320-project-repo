from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from datetime import datetime
import re
import db_helper
import generic_helper

app = FastAPI()
inprogress_orders: dict[str, list] = {}

@app.post("/")
async def handle_request(request: Request): 
    payload = await request.json()
    
    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    output_contexts = payload["queryResult"]["outputContexts"]
    
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])
    
    print(intent)
    
    if intent == "track.order - context: ongoing-tracking":
        response = track_order(parameters, session_id)
    elif intent == "track.order.cancel - context: ongoing-tracking":
        response = cancel_order(parameters, session_id)
    elif intent == "order.add - context: ongoing-order":
        response = add_to_order(parameters, session_id)
    elif intent == "order.remove - context: ongoing-order":
        response = remove_from_order(parameters, session_id)
    elif intent == "order.complete - context: ongoing-order": 
        response = complete_order(parameters, session_id)
        
    return response

def add_to_order(parameters: dict, session_id: str):
    origin_city = parameters["geo-city"]
    destination_city = parameters["geo-city1"]
    number_of_tickets = int(parameters["number"])
    date = datetime.fromisoformat(parameters["date-time"]).date()
    
    new_order = (origin_city, destination_city, number_of_tickets, date)
    if session_id in inprogress_orders:
        inprogress_orders[session_id].append(new_order)
    else:
        inprogress_orders[session_id] = [new_order]
        
    fullfilment_text = generic_helper.get_str_from_order(inprogress_orders[session_id])
    return JSONResponse(content={"fulfillmentText": fullfilment_text + "\n\nWhat would you like to do next?"})
    
def remove_from_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        return JSONResponse(content={"fulfillmentText": "You have no trips in progress. Please say something like \"Create a new trip\" to start planning your trip."})
    
    orders = inprogress_orders[session_id]
    origin_city = parameters["geo-city"]
    destination_city = parameters["geo-city1"]
    
    print("Before removal:", orders)
    for order in orders:
        if order[0] == origin_city and order[1] == destination_city:
            orders.remove(order)
            print("After removal:", orders)
            fullfilment_text = generic_helper.get_str_from_order(orders)
            break
    else:
        fullfilment_text = f"Trip from {origin_city} to {destination_city} not found."
            
    return JSONResponse(content={"fulfillmentText": fullfilment_text})
    
def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        return JSONResponse(content={"fulfillmentText": "You have no trips in progress. Please say something like \"Create a new trip\" to start planning your trip."})
    
    orders = inprogress_orders[session_id]
    if not orders:
        return JSONResponse(content={"fulfillmentText": "You have no trips in progress. Please say something like \"Create a new trip\" to start planning your trip."})
    order_ids = db_helper.save_to_db(orders)
    print(order_ids)
    
    if not order_ids:
        fullfilment_text = "There was an error processing your trips. Please try again."
    else:
        fullfilment_text = f"Your trips(s) have been successfully placed. Your trip id(s) are: {', '.join(list(map(str, order_ids)))}. You may track/manage your trip(s) using the trip id(s)."
    
    del inprogress_orders[session_id]    
    return JSONResponse(content={"fulfillmentText": fullfilment_text})
        
def track_order(parameters: dict, session_id: str):
    order_id = int(parameters["number"])
    status = db_helper.get_order_status(order_id)
    
    if status is None:
        fullfilment_text = f"Order with order_id: {order_id} not found."
    else:
        fullfilment_text = f"Order with order_id: {order_id} is {status}."
    return JSONResponse(content={"fulfillmentText": fullfilment_text})

def cancel_order(parameters: dict, session_id: str):
    order_id = int(parameters["number"])
    status = db_helper.get_order_status(order_id)
    
    if status is None:
        fullfilment_text = f"Order with order_id: {order_id} not found."
    elif status == "canceled":
        fullfilment_text = f"Order with order_id: {order_id} has already been cancelled."
    else:
        flag = db_helper.remove_order(order_id)
        if not flag:
            fullfilment_text = "There was an error cancelling your order. Please try again."
        else:
            fullfilment_text = f"Order with order_id: {order_id} has been successfully cancelled."
    return JSONResponse(content={"fulfillmentText": fullfilment_text})
    

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}