# Import socket module
from socket import *
import threading
import os

# Function to handle client requests
def handle_client(connectionSocket):
    try:
        # Receive the request message from the client
        message = connectionSocket.recv(1024).decode()  # Receive the message
        print(f"Received request:\n{message}")  # Log the request

        # Extract the filename from the request
        filename = message.split()[1]  # GET /index.html HTTP/1.1
        filepath = filename[1:]  # Strip the leading '/'

        # Open the requested file
        with open(filepath, 'rb') as f:  # Open file in binary mode
            outputdata = f.read()  # Read file content

        # Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n")  # HTTP response status
        connectionSocket.send(b"Content-Type: text/html\r\n")  # Set content type
        connectionSocket.send(b"\r\n")  # End of header

        # Send the content of the requested file to the client
        connectionSocket.send(outputdata)

    except IOError:
        # Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")  # Not found status
        connectionSocket.send(b"\r\n")  # End of header
        connectionSocket.send(b"404 Not Found\r\n")  # Body message

    finally:
        # Close client socket
        connectionSocket.close()

# Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8080  # Define the port number
serverSocket.bind(('', serverPort))  # Bind the server to the port
serverSocket.listen(5)  # Listen for incoming connections
print('Server is running on port', serverPort)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accept a connection

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()  # Start the thread to handle the request

# Close the server socket
serverSocket.close()
