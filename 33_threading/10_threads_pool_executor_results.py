import logging
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)


def square(num: int):
    logging.info(f'Calculate square of {num}')
    time.sleep(random.randint(1, 5))
    logging.info(f'Finish square of {num}')
    return num ** 2


numbers_to_square = [2, 4, 6, 8, 10]
with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_number = {executor.submit(square, number): number for number in numbers_to_square}
    squared_numbers = executor.map(square, numbers_to_square)
    print('Original numbers:', numbers_to_square)
    print('Squared numbers:', list(squared_numbers))

    # for future in as_completed(future_to_number):
    #     original_number = future_to_number[future]
    #     squared_number = future.result()
    #     logging.info(f'Number {original_number} squared is: {squared_number}')

logging.info('All numbers are squared')
