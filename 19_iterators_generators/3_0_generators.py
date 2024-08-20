# As usual function returning bunch of results at a time
# Takes memory size of N integers to hold all numbers in list
from typing import Generator


def square_numbers_list(n):
    numbers = []
    for number in range(n + 1):
        numbers.append(number ** 2)

    return numbers


# print(square_numbers_list(3))


# Generator is a function which YIELDS a value
# and saves current state of function
# Takes memory size of 1 integer only,
# no need to keep all of them in memory
def square_numbers_generator(n) -> Generator:
    for number in range(n + 1):
        yield number ** 2


generator = square_numbers_generator(3)

print('Squared numbers from 0 to 3:')

# lazy nature of generators as subtype of iterators
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for square_number in generator:
    print(square_number)


# if we try to continue calling next(),
# program will raise StopIteration exception

# print(next(generator))

