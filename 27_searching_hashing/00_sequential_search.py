# O(N) complexity
import timeit


def sequential_search(array: list[int], element: int) -> int:
    idx = 0
    while idx < len(array):
        if array[idx] == element:
            return idx
        idx += 1

    return -1


array = [num for num in range(-100, 100)]
element = 6
print(sequential_search(array, element))

timer = timeit.timeit(
    stmt=lambda: sequential_search(array, element),
    number=1000000,
)
print(timer)
