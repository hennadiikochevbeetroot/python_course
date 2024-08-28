from main import add, subtract, divide, multiply


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(6, 2) == 3
