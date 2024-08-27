import random
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()

    def __str__(self) -> str:
        took_time = round(float(self.end_time - self.start_time), 3)
        return f'Took {took_time} seconds'


if __name__ == '__main__':
    with Timer() as timer:
        time.sleep(random.randint(1, 5))

    print('Timer:', timer)
