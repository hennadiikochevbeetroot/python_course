import socket

HOST = 'localhost'  # Standard loop-back interface address (localhost) 127.0.0.1
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# HTTP 80, HTTPS 443

# instead of
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ....
# sock.close()
# IPv4 TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # f'', b'data'
            data = conn.recv(1024)
            if not data:
                break
            # Answer
            conn.sendall(data.upper())
