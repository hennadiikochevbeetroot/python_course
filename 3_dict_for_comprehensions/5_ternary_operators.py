# Ternary operators - if else statements on one line
# Syntax: <value_if_true> if <condition> else <value_if_false>

a = 10
b = 20
print('A is less than B' if a < b else 'B is less or equal than A')

math_works = 'Math works' if 1 > 0 else 'Math failed'

num1 = 5
num2 = 10
# Max value getting options:

# Option 1 - 4 lines:
if num1 > num2:
    max_value = a
else:
    max_value = b

# Option 2 - 1 line:
max_value = num1 if num1 > num2 else num2
print('Max value: ', max_value)


# Nested ternary operators - harder to read
# But makes us possible to write cool oneliners
# Another drawback if that debugger cannot get inside of if else logic

nums_compared = 'num1 == num2' if num1 == num2 else 'num1 > num2' if num1 > num2 else 'num1 <= num2'
print(nums_compared)





