import datetime
import random
import time

import pytest


@pytest.fixture(autouse=True)
def log_timer():
    start_time = datetime.datetime.now()
    with open('test.log', 'a') as log_file:
        log_file.write(f'Start time: {start_time}\n')

    yield  # where test functions are called and run

    end_time = datetime.datetime.now()
    with open('test.log', 'a') as log_file:
        log_file.write(f'End time: {end_time}\n')


def test_something_long():
    calculation = 4 ** 2
    time.sleep(random.randint(1, 5))
    assert calculation == 16


def test_other():
    assert True
