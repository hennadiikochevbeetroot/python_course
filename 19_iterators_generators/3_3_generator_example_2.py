from typing import Iterable, Generator


def squared(iterable: Iterable[int | float]) -> Generator[int | float, None, None]:
    for element in iterable:
        yield element ** 2


for current, square in enumerate(squared([1, 2, 3, 4, 5]), 1):
    print(f'Square of {current} is {square}')
