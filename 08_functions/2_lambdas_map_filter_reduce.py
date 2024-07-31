import functools
from typing import Callable

# Lambda = anonymous function
# Syntax: lambda params: return clause

# number: int = 1
#
# add: Callable[[int, int], int] = lambda num1, num2: num1 + num2
#
# # def add(num1, num2):
# #     return num1 + num2
#
# print(add(1, 2))
#
#
# def greater_than_5(num: int) -> bool:
#     return num > 5
#
#
# numbers = [6, 7, 3, 5]
# numbers_greater_than_5 = list(filter(greater_than_5, numbers))
#
# numbers_greater_than_5 = []
# for number in numbers:
#     if greater_than_5(number):
#         numbers_greater_than_5.append(number)
#
#
#
# print('Numbers > 5: ', numbers_greater_than_5)


# def increment(num):
#     return num + 1
#
#
# numbers = [6, 7, 3, 5]
# incremented_numbers = list(map(lambda num: num + 1, numbers))
# print('Numbers + 1: ', incremented_numbers)
#
# incremented_numbers = []
# for number in numbers:
#     incremented_number = increment(number)
#     incremented_numbers.append(incremented_number)


# numbers = [6, 7, 3, 5]
# result = functools.reduce(lambda curr, next: curr + next, numbers)
# print('Result: ', result, type(result))

# numbers_sum = functools.reduce(add, numbers)
# print('Sum: ', numbers_sum)



alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeoiu'


consonants = filter(lambda letter: letter not in vowels, alphabet)
uppercase_consonants = map(lambda letter: letter.upper(), consonants)
consonant_string = functools.reduce(lambda curr, next: curr + next, uppercase_consonants)

print(consonant_string, type(consonant_string))










