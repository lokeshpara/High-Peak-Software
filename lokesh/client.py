# Import socket module
from socket import *
import sys
import time

def main(server_ip, server_port, filename):
    # Create a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    # Measure the time taken to send and receive the request (RTT)
    start_time = time.time()
    
    try:
        # Establish a connection to the server
        clientSocket.connect((server_ip, server_port))
        
        # Send HTTP GET request to the server
        request_line = f"GET /{filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        clientSocket.send(request_line.encode())  # Send the request

        # Receive the server's response
        response = b""  # Initialize an empty byte string
        while True:
            part = clientSocket.recv(1024)  # Receive in chunks of 1024 bytes
            if not part:  # Break if no more data is received
                break
            response += part  # Append to the response
        
        # Measure the Round Trip Time (RTT)
        end_time = time.time()
        rtt = end_time - start_time
        print(f"Round-Trip Time (RTT): {rtt:.6f} seconds")
        
        # Split the response into headers and body
        headers, body = response.split(b'\r\n\r\n', 1)
        
        # Print the status line from the response headers
        status_line = headers.split(b'\r\n')[0]
        print(f"Server response: {status_line.decode()}")

        # Print the body of the response (file content)
        print(body.decode())
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        clientSocket.close()

if __name__ == "__main__":
    # Check the command line arguments for server IP, port, and filename
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_ip> <port> <filename>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    
    main(server_ip, server_port, filename)
