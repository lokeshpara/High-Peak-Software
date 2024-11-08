from socket import *
import time

def request_file(server_ip, port, file_name):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    start_time = time.time()  # Start RTT measurement

    try:
        clientSocket.connect((server_ip, port))
        rtt_start = time.time()

        # Send HTTP GET request
        request = f"GET /{file_name} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        clientSocket.send(request.encode())

        # Receive response from server
        response = clientSocket.recv(4096)
        rtt_end = time.time()  # End RTT measurement

        print(response.decode())

        # Calculate and display RTT
        rtt = (rtt_end - rtt_start) * 1000
        print(f"Round Trip Time (RTT): {rtt:.2f} ms")

        # Display server connection details
        print("Server Details:")
        print(f"Host Name: {server_ip}")
        print(f"Socket Family: {clientSocket.family}")
        print(f"Socket Type: {clientSocket.type}")
        print(f"Protocol: {clientSocket.proto}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        clientSocket.close()
        print("Client connection closed")

if __name__ == "__main__":
    server_ip = "127.0.0.1"
    port = 8080
    file_name = "index.html"
    request_file(server_ip, port, file_name)
