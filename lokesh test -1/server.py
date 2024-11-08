from socket import *
import threading

# Handle client requests in a separate thread
def handle_client(connectionSocket, addr):
    try:
        # Receive the client request
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1][1:]  # Extract filename

        # Open and read the requested file
        with open(filename, 'rb') as f:
            outputdata = f.read()

        # Send HTTP response header
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        
        # Send file content to the client
        connectionSocket.sendall(outputdata)
        
        print(f"File '{filename}' sent to {addr}")

    except IOError:
        # If file is not found, send 404 response
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found")

    finally:
        # Close the connection
        connectionSocket.close()

# Server setup
def start_server(port=8080):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', port))
    serverSocket.listen(5)
    print(f"Server is ready on port {port}")

    while True:
        # Accept a client connection
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection from {addr}")
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
