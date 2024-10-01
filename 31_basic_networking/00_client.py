import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# socket.SOCK_DGRAM - UDP
# socket.SOCK_STREAM - TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))       # Connect to server
    s.sendall(b'Hello, world')    # Send request b'Hello, world'
    data = s.recv(1024)           # Wait for response 'HELLO, WORLD'

print('Received', repr(data))
