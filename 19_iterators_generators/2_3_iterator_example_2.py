class Squared:
    TWO = 2

    def __init__(self, numbers: list[int | float]):
        self.__numbers = numbers
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < len(self.__numbers):
            squared_element = self.__numbers[self.__current_index] ** self.TWO
            self.__current_index += 1
            return squared_element

        raise StopIteration


numbers = [1, 2, 3, 4, 5]
squared = Squared(numbers)
it = iter(squared)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print('-----------------')

# Or simpler:
for square in Squared(numbers):
    print(square)
