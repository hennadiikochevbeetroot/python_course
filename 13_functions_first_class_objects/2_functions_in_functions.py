from typing import Callable


def add_five(num: int) -> int:
    return num + 5


def call_twice(func: Callable) -> Callable:
    def result_func():
        return func(func())

    return result_func


def call_times(func: Callable, times: int) -> Callable:
    def result_func(param):
        result = func(param)
        for _ in range(times - 1):
            print('Current result: ', result)
            result = func(result)

        return result

    return result_func


# add_five_twice = call_twice(add_five)
# print(add_five_twice(57))


add_five_for_six_times = call_times(add_five, 6)
print(add_five_for_six_times(10))
