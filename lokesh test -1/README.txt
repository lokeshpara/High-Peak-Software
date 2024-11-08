# Let's create a README file with the provided content and save it as "README.md".

readme_content = """
# Multi-Threaded Web Server and Single-Threaded Client in Python

### Project Description

This project implements a basic multi-threaded web server that can handle HTTP GET requests from multiple clients simultaneously. A single-threaded client is also included to test server responses and measure round-trip time (RTT).

### Files

- **server.py**: Contains the code for the multi-threaded web server.
- **client.py**: Contains the code for the single-threaded client.

### Prerequisites

- Python 3.x
- Visual Studio Code (or any compatible IDE)

### Instructions

#### Running the Server

1. Open a terminal or command prompt in the directory where `server.py` is located.
2. Run the server with the command:
   ```bash
   python server.py 8080
