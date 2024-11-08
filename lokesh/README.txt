# Project Title: Multi-threaded Web Server and Client in Python

## Project Description
This project includes a multi-threaded HTTP server and a client implemented in Python. The server handles multiple clients simultaneously, serving HTML or text files upon request.

## File Descriptions
- `server.py`: The server code that listens for client connections, handles HTTP GET requests, and sends the requested file back to the client.
- `client.py`: The client code that connects to the server, sends an HTTP GET request for a specific file, and displays the server's response.
- `HelloWorld.html`: A sample HTML file served by the server.
- `README.txt`: Instructions on setting up and running the project.

## Requirements
- Python 3.x
- All files should be in the same directory for easy access.

## Instructions

### Step 1: Run the Server
1. Open a terminal in the project directory.
2. Start the server with the following command:
   ```bash
   python server.py
