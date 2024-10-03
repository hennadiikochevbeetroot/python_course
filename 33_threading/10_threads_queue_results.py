import threading
import queue
import time


def square(num: int, result_queue: queue.Queue):
    print(f"Calculating square of {num}")
    time.sleep(2)
    result_queue.put(num ** 2)  # Put the result in the queue


def square_list(numbers: list[int], result_queue: queue.Queue):
    for num in numbers:
        print(f"Calculating square of {num}")
        time.sleep(0.5)
        result = num ** 2
        result_queue.put(result)


result_queue = queue.Queue()
number_to_square = 7
numbers_to_square = list(range(10))
# t = threading.Thread(target=square, args=(number_to_square, result_queue))
t = threading.Thread(target=square_list, args=(numbers_to_square, result_queue))
t.start()
t.join()

# Retrieve the result from the queue
# result = result_queue.get()
for number in numbers_to_square:
    result = result_queue.get()
    print(f"Number {number} squared is: {result}")
