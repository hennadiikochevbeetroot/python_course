import math
import timeit


# O(sqrt(N)) - only for sorted arrays - is better than O(N), but worse than O(logN)
def jump_search(array: list[int], target: int) -> int:
    array_size = len(array)
    jump_size = int(math.sqrt(array_size))
    block_end = jump_size

    # Search for block where array[block_start] <= target <= array[block_end]
    block_start = 0
    while array[min(block_end, array_size) - 1] < target:
        block_start = block_end
        block_end += jump_size
        if block_start >= array_size:
            return -1

    # Perform a linear search on that
    for idx in range(block_start, min(block_end, array_size)):
        if array[idx] == target:
            return idx

    return -1


array = [num for num in range(-100, 100)]
target = 6
print(jump_search(array, target))

timer = timeit.timeit(
    stmt=lambda: jump_search(array, target),
    number=1000000,
)
print(timer)
