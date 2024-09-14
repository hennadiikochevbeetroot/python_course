# You need to design a recursive function called replicate
# which will receive arguments times and number.
# The function should return an array containing repetitions of the number argument.
# For instance, replicate(3, 5) should return [5,5,5].
# If the times argument is negative, return an empty array.
# As tempting as it may seem, do not use loops to solve this problem.

import itertools

print(list(itertools.repeat(5, 3)))


def replicate_iterative(times: int, number: int) -> list[int]:
    result = []
    for _ in range(times):
        result.append(number)

    return result


print(replicate_iterative(3, 5))


def replicate_recursive(times: int, number: int) -> list[int]:
    if times <= 0:
        # base case
        return []
    # recursive case -> moves the problem to solution (base case)
    return [number] + replicate_recursive(times - 1, number)


print(replicate_recursive(7, 7))
