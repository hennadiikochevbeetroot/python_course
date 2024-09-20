# O(N) complexity
def sequential_search(array: list[int], element: int) -> int:
    idx = 0
    while idx < len(array):
        if array[idx] == element:
            return idx
        idx += 1

    return -1


array = [-100, -1.5, 2, 3, 4, 6, 31, 101]
element = 6
print(sequential_search(array, element))
