import datetime
import os
from contextlib import contextmanager


@contextmanager
def temp_dir():
    original_dir = os.getcwd()

    try:
        dir_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        dir_path = f'{original_dir}/{dir_name}'
        os.mkdir(dir_path)
        os.chdir(dir_path)
        yield
    finally:
        os.chdir(original_dir)


if __name__ == '__main__':
    # with temp_dir():     # Nested CM
    #     with open('main.log', 'w') as log_file:
    #         log_file.write('Log text....')

    with temp_dir(), open('main.log', 'w') as log_file:
        log_file.write('Log text....')
