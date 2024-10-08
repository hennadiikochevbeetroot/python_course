import multiprocessing
import random
import time


# FIFO - what you put first, you get first
def square(numbers: list[int], result_queue: multiprocessing.Queue):
    for number in numbers:
        print(f'Squaring number {number}')
        result = number ** 2
        result_queue.put(result)
    # Final value
    result_queue.put(None)


def read_squared(result_queue: multiprocessing.Queue):
    while True:
        result = result_queue.get()
        if result is None:  # Check for the final value
            break

        print(f'Getting from queue: ', result)


def main():
    numbers = list(range(10))
    queue = multiprocessing.Queue()

    square_process = multiprocessing.Process(target=square, args=(numbers, queue))
    read_process = multiprocessing.Process(target=read_squared, args=(queue,))

    square_process.start()
    read_process.start()

    square_process.join()
    read_process.join()


if __name__ == '__main__':
    main()
