import timeit

# This search technique uses the Fibonacci sequence
# to divide the array into smaller sections,
# leveraging the properties of the sequence
# to perform fewer comparisons.
# 0 1 1 2 3 5 8 13 21 34 55
# O(logN) - only for sorted arrays
def fibonacci_search(array: list[int], target: int) -> int:
    array_size = len(array)

    # Setup fibonacci sequence up until array_size
    fib_first, fib_second, fib_third = 0, 1, 1
    while fib_third < array_size:
        fib_first, fib_second, fib_third = fib_second, fib_third, fib_second + fib_third

    offset = -1
    while fib_third > 1:
        idx = min(offset + fib_first, array_size - 1)

        # If target is greater than the value at index `idx`, cut the subarray after `idx`
        if array[idx] < target:
            fib_third, fib_second, fib_first = fib_second, fib_first, fib_second - fib_first
            offset = idx
        # If target is less than the value at index `idx`, cut the subarray before `idx`
        elif array[idx] > target:
            fib_third, fib_second, fib_first = fib_first, fib_second - fib_first, 2 * fib_first - fib_second
        # Or found
        else:
            return idx

    # Compare the last element with the target
    if fib_second and array[offset + 1] == target:
        return offset + 1

    # Not found
    return -1


array = [num for num in range(-100, 100)]
target = 6
print(fibonacci_search(array, target))

timer = timeit.timeit(
    stmt=lambda: fibonacci_search(array, target),
    number=1000000,
)
print(timer)
