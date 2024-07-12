test_str = 'Test string'

# String is in fact the list of characters
# And each of them may be accessed by index
# In python, indexing starts with zero

print(test_str[0])
print(test_str[1])

# Last string character
print(test_str[-1])

# Accessing string character by index more than possible
# will cause 'Index out of range' error
# print(test_str[45])


# Slicing lets us take part of string
# Syntax is str_var[start:stop_excluding:step]
# All three: start, stop_excluding, step may be omitted
# default start: 0, default end: -1, default step: 1
print(test_str[1:4])
print(test_str[:])
print(test_str[::3])



