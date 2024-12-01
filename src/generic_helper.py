import re

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        return match.group(1)
    return ""

def get_str_from_order(orders: list):
    if not orders:
        return "You have no trips in progress. Please say something like \"Create a new trip\" to start planning your trip."
    
    response_str = f"So far you have {len(orders)} trips(s):\n\n"
    for i, order in enumerate(orders):
        response_str += f"{i+1}. {order[2]} tickets from {order[0]} to {order[1]} on {order[3]}\n"
    return response_str