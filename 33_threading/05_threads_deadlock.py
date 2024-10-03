import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread_1():
    print("[Thread 1] Trying to acquire Lock A...")
    with lock_a:
        print("[Thread 1] Acquired Lock A. Working...")
        time.sleep(1)

        print("[Thread 1] Trying to acquire Lock B...")
        with lock_b:
            print("[Thread 1] Acquired Lock B. Continuing work...")


def thread_2():
    print("[Thread 2] Trying to acquire Lock B...")
    with lock_b:
        print("[Thread 2] Acquired Lock B. Working...")
        time.sleep(1)

        print("[Thread 2] Trying to acquire Lock A...")
        with lock_a:
            print("[Thread 2] Acquired Lock A. Continuing work...")


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed.")
