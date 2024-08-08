import datetime
import random
import time
from functools import wraps
from typing import Callable, Any


def timer(surround: bool = True) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            diff_time = end_time - start_time

            message = f'Took time is: {diff_time}'
            if surround:
                message = f'**********\n{message}\n**********\n'

            print(message)
            return result

        return wrapper

    return decorator


@timer(surround=True)
def sleep_random():
    """Sleeps some time"""
    print('Sleeping')
    time.sleep(random.randint(1, 5))
    print('End sleeping')

    return 42


# sleep_random = timer(surround=True)(sleep_random)
# print(sleep_random.__name__)
# print(sleep_random.__doc__)

result = sleep_random()
print(result)