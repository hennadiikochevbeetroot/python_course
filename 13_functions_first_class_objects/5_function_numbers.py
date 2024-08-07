from typing import Callable


def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


print(f'Add 1 and 2 = {add(1, 2)}')


user_input = input('Enter number: ')  # returns str in any case
