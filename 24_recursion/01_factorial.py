# Iterative
def factorial_iterative(num: int):
    if num <= 0:
        raise ValueError('Factorial cannot be for 0 or less')

    result = 1
    for n in range(2, num + 1):
        result *= n

    return result


def factorial_recursive(num: int):
    if num <= 0:
        raise ValueError('Factorial cannot be for 0 or less')

    if num == 1:
        return 1

    return num * factorial_recursive(num - 1)


def factorial_recursive_oneliner(num: int):
    if num <= 0: raise ValueError('Factorial cannot be for 0 or less')
    return 1 if num == 1 else num * factorial_recursive(num - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
print(factorial_recursive_oneliner(5))
