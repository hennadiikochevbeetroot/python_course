import socket


class MyServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def __enter__(self):
        # IPv4 TCP Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def answer_with_uppercase(self):
        print('Ready to answer...')
        # Wait for incoming connection
        conn, address = self.sock.accept()
        with conn:
            print(f'Incoming connection by client')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Server received data: ', data)
                processed_data = data.upper()
                conn.sendall(processed_data)
                print('Server sends after processing: ', processed_data)


with MyServer(host='localhost', port=65432) as myserver:
    myserver.answer_with_uppercase()
