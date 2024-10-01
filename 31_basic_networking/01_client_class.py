import socket


class MySocket:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def send_message_receive_answer(self, msg: str):
        self.sock.sendall(msg.encode())
        answer = self.sock.recv(1024)
        return answer


with MySocket(host='127.0.0.1', port=65432) as mysocket:
    answer = mysocket.send_message_receive_answer('Hello from client!')
    print('Answer received: ', answer)
