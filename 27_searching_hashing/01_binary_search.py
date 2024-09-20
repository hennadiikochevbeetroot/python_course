import timeit


# O(logN) - only for sorted arrays
def binary_search(array: list[int], target: int) -> int:
    start, end = 0, len(array) - 1

    while start < end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        else:
            if target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


array = [num for num in range(-100, 100)]
target = 6
print(binary_search(array, target))

timer = timeit.timeit(
    stmt=lambda: binary_search(array, target),
    number=1000000,
)
print(timer)
