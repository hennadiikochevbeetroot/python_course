import threading
import random
import string
import time


def random_string(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def short_business_logic(param1: str, param2: str, time_to_take: int):
    # getName() method is deprecated
    thread_name = threading.current_thread().name
    time.sleep(time_to_take)  # I/O operation
    print(f'({thread_name}) Short Business logic with param1: {param1}, param2: {param2}')


def long_business_logic(param1: str, param2: str):
    thread_name = threading.current_thread().name
    time.sleep(5)  # I/O operation
    print(f'({thread_name}) Long Business logic with param1: {param1}, param2: {param2}')


threads = []
for time_to_take in range(3):
    param1, param2 = random_string(), random_string()
    thread = threading.Thread(name=f'Thread{time_to_take}', target=short_business_logic,
                              args=(param1, param2, time_to_take))
    thread.start()
    threads.append(thread)

param1, param2 = random_string(), random_string()
long_thread = threading.Thread(name=f'Long Thread', target=long_business_logic, args=(param1, param2))
long_thread.start()
threads.append(long_thread)


for thread in threads:
    thread.join()     # If we wouldn't join, below print statement would work before threads finish

print('All threads finished their work')

