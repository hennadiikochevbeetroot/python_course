from typing import Generator


def fibonacci(threshold: int = 15) -> Generator[int, None, None]:
    current, next = 0, 1
    for _ in range(threshold):
        yield current
        current, next = next, current + next


for current, fib in enumerate(fibonacci(20), 1):
    print(f'Fibonacci number {current} is {fib}')
