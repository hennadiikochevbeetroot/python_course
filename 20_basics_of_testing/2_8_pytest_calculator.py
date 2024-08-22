from classes_to_test import Calculator
import pytest


def test_add():
    two = Calculator.add(1, 1)
    assert two == 2


def test_subtract():
    three = Calculator.subtract(5, 2)
    assert three == 3


def test_multiply():
    eight = Calculator.multiply(2, 4)
    assert eight == 8


def test_divide_non_zero():
    four = Calculator.divide(12, 3)
    assert four == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        Calculator.divide(5, 0)

    assert str(exc_info.value) == 'Num2 cannot be zero'
