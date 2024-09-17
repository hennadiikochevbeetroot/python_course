# Euclid's algorithm
# Swap num2 with num1 and remainder of num1 / num2
# 98, 56 example
# 56, 98 % 56=(42)
# 42, 56 % 42=(14)
# 14, 42 % 14=(0)
# Answer is 14


def gcd_iterative(num1: int, num2: int):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_recursive(num1: int, num2: int):
    if num2 == 0:
        # base case
        return num1
    else:
        # recursive
        return gcd_recursive(num2, num1 % num2)


def gcd_recursive_oneliner(num1: int, num2: int):
    return num1 if num2 == 0 else gcd_recursive_oneliner(num2, num1 % num2)


a = 56
b = 98

print(gcd_iterative(a, b))
print(gcd_recursive(a, b))
print(gcd_recursive_oneliner(a, b))

