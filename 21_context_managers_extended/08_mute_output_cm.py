import os
from contextlib import contextmanager
from decimal import Decimal, localcontext
import sys


@contextmanager
def mute_output():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    # echo "text" > /dev/null
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


with mute_output():
    print('This will not be printed')

print('But this will be printed')


def default_decimal_precision_calc():
    print('Default precision')
    num1 = Decimal(2)
    num2 = Decimal(3)
    print(num1 / num2)


def custom_decimal_precision_calc(precision: int):
    print('Custom precision: ', precision)
    with localcontext(prec=precision):
        num1 = Decimal(2)
        num2 = Decimal(3)
        print(num1 / num2)
