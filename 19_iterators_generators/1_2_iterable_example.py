from collections.abc import Iterable

class Numbers:
    def __init__(self, *numbers: int):
        self.__numbers = numbers

    def __getitem__(self, index: int) -> int:
        if index < len(self.__numbers):
            return self.__numbers[index]

        raise IndexError(f'No such index: {index} in this list')


numbers = Numbers(1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)


print(numbers[3])


