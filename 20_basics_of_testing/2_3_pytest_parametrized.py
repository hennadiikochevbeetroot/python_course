import pytest


def add(num1: int, num2: int) -> int:
    return num1 + num2


def loggify(text: str) -> str:
    return f'LOG: {text}'


# @pytest.mark.parametrize(
#     'text',
#     [
#         'Text1',
#         'Example2',
#         'SomeText3',
#     ]
# )

@pytest.mark.parametrize('text', ['Text1',
                                  'Example2',
                                  'SomeText3'])
def test_loggify(text: str):
    assert loggify(text) == 'LOG: ' + text


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (2, 2, 4),
        (3, 5, 8),
        (6, 9, 15),
    ]
)
def test_math_addition(num1: int, num2: int, result: int):
    assert add(num1, num2) == result
