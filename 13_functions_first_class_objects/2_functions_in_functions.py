from typing import Callable


def add_five(num: int) -> int:
    return num + 5


def call_twice(func: Callable) -> Callable:
    def result_func(*args, **kwargs):
        return func(func(*args, **kwargs))

    return result_func


add_five_twice = call_twice(add_five)
print(add_five_twice(57))
