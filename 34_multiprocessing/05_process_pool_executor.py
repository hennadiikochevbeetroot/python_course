import logging
import time
from concurrent.futures import ProcessPoolExecutor
import os

logging.basicConfig(level=logging.INFO)

def square(number: int):
    """Function to square a number."""
    logging.info(f"Process ID: {os.getpid()} computing square of {number}")
    time.sleep(1)
    return number ** 2


def main():
    numbers = list(range(10))

    with ProcessPoolExecutor(max_workers=5) as executor:
        future = executor.submit(square, 5)
        single_result = future.result()
        logging.info(f'Single result: {single_result}')

        multiple_results = list(executor.map(square, numbers))
        logging.info(f"Original numbers: {numbers}")
        logging.info(f"Squared numbers: {multiple_results}")


if __name__ == '__main__':
    main()
