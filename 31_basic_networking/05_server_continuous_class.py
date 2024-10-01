import socket


class MyContinuousServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        # Only 1 connection at a time
        self.sock.listen(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def answer_multiple_uppercase(self):
        print('Ready to answer...')
        while True:
            conn, address = self.sock.accept()
            with conn:
                print('Connected by client')
                data = conn.recv(1024)
                print('Server Received: ', data)
                processed_data = data.upper()
                conn.sendall(processed_data)
                print('Server sent back:', processed_data)

                if 'stop' in str(data).lower():
                    print('Received stop signal, exiting server')
                    break


with MyContinuousServer(host='localhost', port=65432) as myserver:
    myserver.answer_multiple_uppercase()
