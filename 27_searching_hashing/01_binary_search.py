import timeit


def binary_search(array: list[int], element: int):
    start, end = 0, len(array) - 1

    while start < end:
        mid = (start + end) // 2
        if array[mid] == element:
            return mid
        else:
            if element < array[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


array = [num for num in range(-100, 100)]
element = 6
print(binary_search(array, element))

timer = timeit.timeit(
    stmt=lambda: binary_search(array, element),
    number=1000000,
)
print(timer)
