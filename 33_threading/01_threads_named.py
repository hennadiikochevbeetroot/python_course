import threading
import random
import string


def random_string(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def business_logic(param1: str, param2: str):
    # getName() method is deprecated
    thread_name = threading.current_thread().name
    print(f'({thread_name}) Business logic with param1: {param1}, param2: {param2}')


for count in range(5):
    param1, param2 = random_string(), random_string()
    thread = threading.Thread(name=f'Thread{count}', target=business_logic, args=(param1, param2))
    thread.start()
