import pytest


@pytest.fixture
def fibonacci_first_10() -> list[int]:
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
