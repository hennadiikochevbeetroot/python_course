import multiprocessing
import multiprocessing.connection
import os


def sender(connection: multiprocessing.connection.Connection, messages: list[str]):
    for message in messages:
        connection.send(message)
        print(f"Sent the message: {message} from process {os.getpid()}")
    connection.close()


def receiver(connection: multiprocessing.connection.Connection):
    while True:
        message = connection.recv()
        if message == "END":
            break
        print(f"Received the message: {message} in process {os.getpid()}")


def main():
    messages = ["hello", "hey", "hru?", "END"]

    sender_connection, receiver_connection = multiprocessing.Pipe()

    sender_process = multiprocessing.Process(target=sender, args=(sender_connection, messages))
    receiver_process = multiprocessing.Process(target=receiver, args=(receiver_connection,))

    sender_process.start()
    receiver_process.start()
    sender_process.join()
    receiver_process.join()


if __name__ == '__main__':
    main()
