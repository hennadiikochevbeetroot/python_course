def binary_search_iterative(arr: list[int], target: int):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


a_list = [el for el in range(0, 101, 5)]
print(a_list)
print(binary_search_iterative(a_list, 35))
print(binary_search_recursive(a_list, 35, 0, len(a_list) - 1))









