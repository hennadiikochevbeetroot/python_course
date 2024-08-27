import time
from contextlib import contextmanager
import random


@contextmanager
def timer():
    start_time = time.time()
    result = {}
    try:
        yield result
    finally:
        end_time = time.time()
        took_time = round(float(end_time - start_time), 3)
        result['message'] = f'Took {took_time} seconds'


if __name__ == '__main__':
    with timer() as t:
        time.sleep(random.randint(1, 5))

    print(t['message'])
