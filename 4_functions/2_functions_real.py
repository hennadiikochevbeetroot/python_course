# Use typehinting!
# It helps both you and IDE to recognize what
# parameter is and returned value is

import random
from typing import Any, Callable, Iterable


def add(num1: int, num2: int) -> int:
    return num1 + num2


# Specifying different types
def multiply(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


# Default values and typehint of container data types
def key_value_str_to_dict(key: str = '', value: str = '') -> dict[str, str]:
    return {key: value}


def duplicate_list(value: str = 'value', times: int = 10) -> list[str]:
    return [value for _ in range(times)]


# No return statement == returns None implicitly
def pretty_print(value: str = '') -> None:
    print(f'--------- {value} ---------')


# If not sure about some type - use Any
def to_set(iterable: Iterable[Any]) -> set[Any]:
    return set(iterable)


# If function is in parameter or returning value - use Callable
def random_math(a: int, b: int) -> Callable:
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    return random.choice([add, sub, mul])


func = random_math(2, 3)
print(func())
