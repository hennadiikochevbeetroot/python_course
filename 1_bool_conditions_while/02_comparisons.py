# Comparisons
# Operations which return a boolean value
# either True or False

# less than
print(0 < 1)
print(1 <= 1)

# Greater than
print(1 > 0)
print(1 >= 1)

# Equality check
print(3 == 3)
print(4 != 5)

# Is, is not
# Used with True, False, None values
a = True
print(a is True)
print(a is not False)
print(a is not None)

# Complex comparison
print(3 < 4 < 5)
print(5 > 4 > 3)

# Combining comparisons with boolean operators
# Comparison has higher priority, executed first
print(False or 0 < 1)
