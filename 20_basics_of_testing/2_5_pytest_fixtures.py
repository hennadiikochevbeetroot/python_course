import pytest


# Fixtures are functions which are run before test execution
# By default, mst fixtures are being put into conftest.py
# And therefore not imported, but instead read by pytest

@pytest.fixture
def list_0_to_10() -> list[int]:
    return list(range(11))


def test_list_length(list_0_to_10):
    assert len(list_0_to_10) == 11


def test_fibonacci_first_10(fibonacci_first_10):
    assert len(fibonacci_first_10) == 10
    assert all(isinstance(num, int) for num in fibonacci_first_10)
