
import timeit


# O(N) complexity - unsorted arrays
def sequential_search(array: list[int], target: int) -> int:
    idx = 0
    while idx < len(array):
        if array[idx] == target:
            return idx
        idx += 1

    return -1


array = [num for num in range(-100, 100)]
target = 6
print(sequential_search(array, target))

timer = timeit.timeit(
    stmt=lambda: sequential_search(array, target),
    number=1000000,
)
print(timer)
