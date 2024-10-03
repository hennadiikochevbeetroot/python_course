import threading
import queue
import time


def square(num: int, result_queue: queue.Queue):
    print(f"Calculating square of {num}")
    time.sleep(2)
    result_queue.put(num ** 2)  # Put the result in the queue


result_queue = queue.Queue()
number_to_square = 7
t = threading.Thread(target=square, args=(number_to_square, result_queue))
t.start()
t.join()

# Retrieve the result from the queue
result = result_queue.get()
print(f"Number {number_to_square} squared is: {result}")
