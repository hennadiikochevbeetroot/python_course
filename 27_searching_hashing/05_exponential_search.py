import timeit


# Exponential search is useful for
# unbounded or infinite-size arrays,
# where you don’t know the size of the array in advance

# O(logN) in any case, based on binary search
# Better if target is closer to beginning

def binary_search(array: list[int], target: int, start: int, end: int) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def exponential_search(array: list[int], target: int) -> int:
    if array[0] == target:
        return 0

    # Find the range where the target might exist by doubling the index
    index = 1
    while index < len(array) and array[index] <= target:
        index *= 2

    # Perform binary search in the found range
    return binary_search(array, target, index // 2, min(index, len(array) - 1))


array = [num for num in range(-100, 100)]
target = 6
print(exponential_search(array, target))

timer = timeit.timeit(
    stmt=lambda: exponential_search(array, target),
    number=1000000,
)
print(timer)

