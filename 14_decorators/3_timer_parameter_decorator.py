import datetime
import random
import time
from functools import wraps
from typing import Callable


def timer(surround: bool = True):
    def timer_deco(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = datetime.datetime.now()
            func(*args, **kwargs)
            end_time = datetime.datetime.now()
            diff_time = end_time - start_time

            message = f'Diff time is: {diff_time}'
            if surround:
                message = f'**********\n{message}\n**********\n'

            print(message)

        return inner

    return timer_deco


# @timer(surround=True)
def sleep_random():
    """Sleeps some time"""
    print('Sleeping')
    time.sleep(random.randint(1, 5))
    print('End sleeping')


sleep_random = timer(surround=True)(sleep_random)



print(sleep_random.__name__)
print(sleep_random.__doc__)

sleep_random()
