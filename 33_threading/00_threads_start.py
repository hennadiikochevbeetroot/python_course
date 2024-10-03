import threading
import random
import string
import time

import requests


def random_string(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def business_logic(param1: str, param2: str):
    response = requests.get('https://api.github.com')
    print(f'Business logic with param1: {param1}, param2: {param2}, resp length = {len(response.content)}')


# param1 = 'string1'
# param2 = 'string2'
# thread = threading.Thread(target=business_logic, args=(param1, param2))
# thread.start()


for count in range(100):
    param1, param2 = random_string(), random_string()
    thread = threading.Thread(target=business_logic, args=(param1, param2))
    thread.start()


# for count in range(100):
#     param1, param2 = random_string(), random_string()
#     business_logic(param1, param2)
