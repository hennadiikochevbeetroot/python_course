import random
import time


class Timer:
    def __enter__(self):
        print('Timer start...')
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Timer end...')
        self.end_time = time.time()

    @property
    def diff_time(self):
        return round(float(self.end_time - self.start_time), 2)

    def __str__(self) -> str:
        took_time = float(self.end_time - self.start_time)
        return f'Took {took_time} seconds'


if __name__ == '__main__':
    with Timer() as timer:    # save start_time
        time.sleep(random.randint(1, 5))

    print('Diff: ', timer.diff_time)
    # save stop_time
    print('Timer:', timer)
