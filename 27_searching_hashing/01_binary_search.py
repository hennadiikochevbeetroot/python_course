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


array = [-100, -1.5, 2, 3, 4, 6, 31, 101]
element = 6
print(binary_search(array, element))
