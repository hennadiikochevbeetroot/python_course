# Booleans - True, False

print(True, type(True))
print(False, type(False))

# Boolean operators: not, and, or
# They are executed in that order if combined,
# but if brackets are present, they are first priority


# Or (Always tries best to find True)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# And (True only if everything passed is True)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Not (Negates value, makes True to be False and vice versa)
print(not True)
print(not False)

# Combining them
print(not True and False or True)
print(True and not False or False)
print((True or False) or not False and True)

# Way that `and` operator works:
# if it meets False argument, then it does not
# evaluate next ones (because it's already obvious
# that total result will be False)
print(False and True and True and True)
