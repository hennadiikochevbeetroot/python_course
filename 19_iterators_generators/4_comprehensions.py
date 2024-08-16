
# List comprehension
# Takes N int memory
square_numbers_list = [number ** 2 for number in range(4)]
print(square_numbers_list)

# Generator comprehension is another way to create a generator
# Takes one int memory
square_numbers = (number ** 2 for number in range(4))

print(square_numbers)

print(next(square_numbers))
print(next(square_numbers))
print(next(square_numbers))
print(next(square_numbers))

# if we try to continue calling next(),
# program will raise StopIteration exception

# print(next(square_numbers))
