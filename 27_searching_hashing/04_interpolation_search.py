import timeit

# Interpolation Search is an improved variant of binary search
# that works on sorted arrays. Instead of always dividing the array into two halves
# (like binary search), interpolation search tries to estimate the position of the target
# element by using the values at the start and end of the array,
# assuming a uniform distribution of elements.

# O(log(logN)) - only for sorted and uniformly distributed data
# 8 - 3 - 1
# 16 - 4 - 2
# 1024 - 10 - 3

def interpolation_search(array: list[int], target: int) -> int:
    start, end = 0, len(array) - 1

    while start <= end and array[start] <= target <= array[end]:
        if start == end:
            # Either found or not
            return start if array[start] == target else -1

        pos = start + ((target - array[start]) * (end - start) // (array[end] - array[start]))
        if array[pos] == target:
            return pos

        if array[pos] < target:
            start = pos + 1
        else:
            end = pos - 1

    # Not found
    return -1


array = [num for num in range(-100, 100)]
target = 6
print(interpolation_search(array, target))

timer = timeit.timeit(
    stmt=lambda: interpolation_search(array, target),
    number=1000000,
)
print(timer)
