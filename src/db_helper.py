import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fdfz0828!!!",
    database="utd_nlp_trip_planning"
)

def save_to_db(orders: list):
    # orders = [(), (), ...]
    cursor = cnx.cursor()
    
    new_order_ids: list[int] = []
    for order in orders:
        origin_city, destination_city, number_of_tickets, date = order
        order_id = get_next_order_id()
        new_order_ids.append(order_id)
        query = f"INSERT INTO Orders (order_id, origin_city, destination_city, number_of_tickets, date) VALUES ({order_id}, '{origin_city}', '{destination_city}', {number_of_tickets}, '{date}')"
        cursor.execute(query)
        cnx.commit()
        
    for order_id in new_order_ids:
        query = f"INSERT INTO OrderTracking (order_id, status) VALUES ({order_id}, 'active')"
        cursor.execute(query)
        cnx.commit()
        
    return new_order_ids
        
def get_next_order_id():
    cursor = cnx.cursor()

    query = "SELECT MAX(order_id) FROM Orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()

    if result is None:
        return 1
    else:
        return result + 1

def get_order_status(order_id: int):
    cursor = cnx.cursor()

    query = f"SELECT status FROM OrderTracking WHERE order_id = {order_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]
    else:
        return None
    
def remove_order(order_id: int):
    try:
        cursor = cnx.cursor()

        query = f"DELETE FROM Orders WHERE order_id = {order_id}"
        cursor.execute(query)
        cnx.commit()
        
        # update the status from active to cancelled in OrderTracking
        query = f"UPDATE OrderTracking SET status = 'canceled' WHERE order_id = {order_id}"
        cursor.execute(query)
        cnx.commit()
        
        cursor.close()

        return True
    except Exception as e:
        print(e)
        return False

