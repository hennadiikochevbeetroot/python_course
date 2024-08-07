import datetime
import random
import time
from functools import wraps
from typing import Callable


def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print('Diff time: ', end_time - start_time)

    return wrapper


@timer
def sleep_random():
    """Sleeps some time"""
    print('Sleeping')
    time.sleep(random.randint(1, 5))
    print('End sleeping')


print(sleep_random.__name__)
print(sleep_random.__doc__)

sleep_random()
