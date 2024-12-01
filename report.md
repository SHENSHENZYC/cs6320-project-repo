# **Developing a Customized Chatbot for Trip Planning Using Dialogflow and FastAPI**

## **Abstract**

This report details the development of a customized chatbot named **Azem-for-Trip-Planning**, designed to assist users in planning trips by creating and managing orders through natural language interactions. The chatbot leverages Dialogflow as the conversational interface and FastAPI as the backend server, interfacing with a MySQL database for data persistence. The project explores beyond baseline functionalities by addressing challenges in intent handling, session management, and database interactions. Innovations include a streamlined session management approach and customized response generation. Complexity arises in integrating multiple technologies and ensuring robust error handling. The report concludes with lessons learned, potential improvements, and an overview of user testing conducted outside the development team.

---

## **1. Introduction**

Travel planning often involves numerous steps, from booking tickets to managing itineraries. Automating this process through a conversational agent can enhance user experience by providing a seamless and interactive platform for trip planning. This project aims to develop a chatbot, Azem-for-Trip-Planning, that allows users to create, track, and manage trip orders using natural language.

---

## **2. System Architecture**

The chatbot system comprises the following components:

- **Dialogflow**: Serves as the Natural Language Understanding (NLU) platform to interpret user intents and entities.
- **FastAPI**: Acts as the backend server to handle HTTP requests from Dialogflow and perform business logic.
- **MySQL Database**: Stores order information and tracking statuses.
- **Python Modules**:
  - `main.py`: Contains the FastAPI application and intent handling logic.
  - `db_helper.py`: Facilitates database operations such as saving orders and querying statuses.
  - `generic_helper.py`: Provides utility functions for session management and response formatting.

---

## **3. Implementation Details**

### **3.1. Intent Handling and Session Management**

The `main.py` script defines an endpoint to handle POST requests from Dialogflow. It processes various intents:

- **Order Creation**:
  - `order.add - context: ongoing-order`: Adds trips to the current session's order.
  - `order.remove - context: ongoing-order`: Removes trips from the current session's order.
  - `order.complete - context: ongoing-order`: Finalizes the order and saves it to the database.

- **Order Tracking**:
  - `track.order - context: ongoing-tracking`: Retrieves the status of a specific order.
  - `track.order.cancel - context: ongoing-tracking`: Cancels a specific order.

Session IDs are extracted from the request context to maintain user-specific interactions using the `extract_session_id` function in `generic_helper.py`. In-progress orders are stored in the `inprogress_orders` dictionary, keyed by session IDs.

### **3.2. Database Operations**

The `db_helper.py` module manages database interactions:

- **Saving Orders**: The `save_to_db` function inserts new orders into the `Orders` table and updates the `OrderTracking` table with an initial status of 'active'.
- **Order Status Retrieval**: The `get_order_status` function fetches the current status of an order.
- **Order Cancellation**: The `remove_order` function deletes the order from the `Orders` table and updates its status to 'canceled' in the `OrderTracking` table.
- **Order ID Management**: The `get_next_order_id` function ensures unique order IDs by retrieving the maximum existing ID and incrementing it.

### **3.3. Response Generation**

Custom responses are crafted to provide meaningful feedback to the user:

- **Order Summaries**: The `get_str_from_order` function in `generic_helper.py` compiles a summary of the current trips in progress.
- **Error Handling**: Appropriate messages are returned when actions cannot be completed, such as attempting to remove a trip not in the order.

---

## **4. Challenges and Solutions**

### **4.1. Intent Disambiguation**

**Issue**: Similar user inputs could trigger incorrect intents, causing confusion in order processing.

**Solution**: Refined intent definitions and contexts in Dialogflow to ensure accurate intent detection. Implemented explicit context management in `main.py` to handle intents appropriately.

### **4.2. Session Consistency**

**Issue**: Maintaining consistent session data across multiple user interactions was challenging due to stateless HTTP requests.

**Solution**: Utilized session IDs extracted from Dialogflow's context to persist user-specific data in the `inprogress_orders` dictionary, ensuring continuity in the user's session.

### **4.3. Database Transaction Management**

**Issue**: Incomplete transactions could lead to data inconsistency, especially when multiple orders are processed simultaneously.

**Solution**: Implemented transaction handling in `db_helper.py` with commit operations after each database interaction. Used try-except blocks to catch exceptions and rollback transactions if necessary.

---

## **5. Innovation and Creativity**

### **5.1. Customized Session Management**

Developed a unique method for session handling by parsing session IDs directly from Dialogflow's context names, which streamlined session tracking without additional overhead or reliance on external storage.

### **5.2. Dynamic Response Construction**

Created personalized and dynamic responses that reflect the user's current order status, enhancing user engagement and providing a conversational experience that mimics human interaction.

---

## **6. Complexity Highlights**

### **6.1. Integration of Multiple Technologies**

Combining Dialogflow, FastAPI, and MySQL required careful consideration of data formats, asynchronous operations, and compatibility between systems. Ensuring seamless communication between the NLU platform and the backend demanded an in-depth understanding of each component.

### **6.2. Error Handling and Validation**

Implemented comprehensive error handling to manage unexpected inputs and database errors gracefully. Validated user inputs at multiple stages to prevent SQL injection and ensure data integrity.

---

## **7. Lessons Learned and Future Improvements**

### **7.1. Importance of Robust Session Handling**

Effective session management is crucial in conversational agents to maintain context and provide a coherent user experience. Future improvements could involve using a dedicated session store or database to handle scalability.

### **7.2. Enhancing Scalability and Performance**

As the user base grows, the current in-memory session storage may become a bottleneck. Migrating to a distributed caching system like Redis could improve performance and scalability.

### **7.3. Expanding Functionality**

Adding features such as itinerary suggestions, integration with external APIs for real-time ticket availability, and user authentication would enhance the chatbot's utility.

---

## **8. User Testing and Feedback**

The chatbot was tested with five individuals outside the development team to gather feedback on usability and functionality.

### **8.1. Test Results**

- **Ease of Use**: Users found the chatbot intuitive and easy to interact with, appreciating the natural language capabilities.
- **Functionality**: All users were able to create and manage orders successfully.
- **Areas for Improvement**: Some users suggested adding more conversational variations and handling ambiguous inputs more effectively.

### **8.2. Feedback Integration**

Based on the feedback, plans are in place to:

- Expand the training phrases in Dialogflow to cover a broader range of user expressions.
- Implement more robust intent disambiguation strategies.

---

## **9. Conclusion**

The Azem-for-Trip-Planning chatbot successfully demonstrates how conversational agents can facilitate trip planning through natural language interactions. By integrating Dialogflow with a FastAPI backend and a MySQL database, the project delivers a cohesive system that handles order creation, tracking, and cancellation. Challenges in intent handling and session management were addressed through innovative solutions, resulting in a user-friendly and efficient chatbot. Future work will focus on enhancing scalability, expanding features, and incorporating user feedback to further improve the system.

---

## **References**

- **Dialogflow Documentation**: [https://cloud.google.com/dialogflow/docs](https://cloud.google.com/dialogflow/docs)
- **FastAPI Documentation**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **MySQL Connector/Python Developer Guide**: [https://dev.mysql.com/doc/connector-python/en/](https://dev.mysql.com/doc/connector-python/en/)

---

## **Appendices**

### **Appendix A: Code Structure Overview**

- **`sow.txt`**: Scope of work outlining the chatbot's functionalities.
- **`main.py`**: Main application script handling HTTP requests and intents.
- **`db_helper.py`**: Database helper module for MySQL operations.
- **`generic_helper.py`**: Utility functions for session extraction and response formatting.

### **Appendix B: Database Schema**

- **`Orders` Table**:
  - `order_id` (INT, PRIMARY KEY)
  - `origin_city` (VARCHAR)
  - `destination_city` (VARCHAR)
  - `number_of_tickets` (INT)
  - `date` (DATE)

- **`OrderTracking` Table**:
  - `order_id` (INT, PRIMARY KEY)
  - `status` (ENUM('active', 'canceled'))

---
