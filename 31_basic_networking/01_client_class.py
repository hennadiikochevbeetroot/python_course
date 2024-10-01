import socket


class MyClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def __enter__(self):
        # IPv4 TCP Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def send_message_receive_answer(self, msg: str):
        self.sock.sendall(msg.encode())
        answer = self.sock.recv(1024)
        return answer


with MyClient(host='localhost', port=65432) as myclient:
    msg = 'Hello from client!'
    print('Client sends message to server:', msg)
    answer = myclient.send_message_receive_answer(msg)
    print('Client received answer from server: ', answer)
