import datetime
from decimal import Decimal
from functools import wraps
from math import factorial
from typing import Callable


def log(file_name: str = 'main.log'):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'a') as log_file:
                log_file.write(f'{datetime.datetime.now()} LOG: {func.__name__} call result is: {result}\n')

            return result

        return wrapper

    return decorator


@log('second.log')
def calculate_pi_with_precision(digits: int = 10) -> Decimal:
    """Calculates PI number up to needed precision"""
    pi = Decimal(0)

    for k in range(digits):
        t = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 545140134 * k)
        deno = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(t) / Decimal(deno)

    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1 / pi

    return round(pi, digits)


calculate_pi_with_precision(20)
