# Iterative
# 5! = 1 * 2 * 3 * 4 * 5
# 0! = 1, 1! = 1
def factorial_iterative(num: int):
    if num == 0:
        return 1

    if num < 0:
        raise ValueError('Factorial cannot be for 0 or less')

    result = 1
    # O(N)
    for n in range(2, num + 1):
        result *= n

    return result


def factorial_recursive(num: int):
    if num <= 0:
        raise ValueError('Factorial cannot be for 0 or less')

    # base case
    # O(1)
    if num in [0, 1]:
        return 1

    # recursive case
    # O(N - 1) + O(N - 2) + O(N - 3) + O(1) = O(N)
    return num * factorial_recursive(num - 1)


def factorial_recursive_oneliner(num: int):
    if num <= 0: raise ValueError('Factorial cannot be for 0 or less')
    return 1 if num in [0, 1] else num * factorial_recursive(num - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
print(factorial_recursive_oneliner(5))
