import multiprocessing
import os
import random
import string


def random_string(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def business_logic(param1: str, param2: str):
    print(f'Parent: {os.getppid()}, process: {os.getpid()} - Business logic with param1: {param1}, param2: {param2}')


if __name__ == '__main__':
    processes = []
    for count in range(5):
        param1, param2 = random_string(), random_string()
        process = multiprocessing.Process(target=business_logic, args=(param1, param2))
        processes.append(process)
        process.start()  # Non-blocking

    for process in processes:
        process.join()   # Blocking

    print('All processes finished')
