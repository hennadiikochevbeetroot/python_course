import functools

# Lambda = anonymous function
# Syntax: lambda params: return clause


add = lambda num1, num2: num1 + num2

print(add(1, 2))

numbers = [6, 7, 3, 5]
numbers_greater_than_5 = list(filter(lambda num: num > 5, numbers))
print('Numbers > 5: ', numbers_greater_than_5)

incremented_numbers = list(map(lambda num: num + 1, numbers))
print('Numbers + 1: ', incremented_numbers)

numbers_sum = functools.reduce(lambda num1, num2: num1 + num2, numbers)
print('Sum: ', numbers_sum)

numbers_sum = functools.reduce(add, numbers)
print('Sum: ', numbers_sum)
