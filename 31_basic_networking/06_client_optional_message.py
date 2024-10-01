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

    def user_input(self):
        pass


while True:
    message = input('Input data to send, or 0 to exit: ').strip()
    if message == '0':
        print('Exiting...')
        break

    with MyClient(host='localhost', port=65432) as myclient:
        answer = myclient.send_message_receive_answer(message)
        print('Client received answer: ', answer)
