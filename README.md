# Django Real Time Chat Application

This is a real-time chat application built with Django, Channels, Redis, and Daphne.

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/OmarEhab177/Chat-app-by-user-id.git
   cd Chat-app-by-user-id
   ```

2. **Install dependencies:**
   You need to install the following dependencies to run this application:
   - Django>=3.2.4,<3.3
   - channels-redis==4.1.0
   - uvicorn==0.22.0
   - websockets==11.0.3
   - daphne==4.0.0
   
   You can install these dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Setup Redis:**
   This application uses Redis as its Channels layer backend. Make sure you have Redis installed and running on your machine.

4. **Apply migrations:**
   Run the following command to apply migrations:
   ```
   python manage.py migrate
   ```

## Running the Application

Run the application using the following command:
```
python manage.py runserver
```
This command will run the Django server with Daphne.

## Using the Application

To start a chat between two users, both users should connect to the socket at the same time. The WebSocket consumer in this application handles the connection, messaging, and disconnection events.

When a user sends a message, it is sent to a group specific to the two chatting users. This group is identified by a room group name, which is a combination of the two users' IDs.

The application also handles the case when a user disconnects by removing them from the room group.
