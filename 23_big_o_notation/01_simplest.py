def contains(array: list[int], x: int) -> bool:
    # O(N) complexity - N is size of array
    for element in array:
        if element == x:
            return True

    return False


def print_pairs(array: list[int]) -> None:
    # O(N^2) complexity
    for x in array:
        for y in array:
            print('Pair: ', x, y)


def find_max_print_pairs(array: list[int]) -> None:
    # O(N) complexity
    max_value = None
    for element in array:
        max_value = max(max_value, element)
    print('Maximum: ', max_value)

    # O(N^2) complexity
    for x in array:
        for y in array:
            print('Pair: ', x, y)


def find_max_with_line_print(array: list[int]) -> None:
    # O(3) complexity
    for i in range(3):
        print('-----------------')

    # O(N) complexity
    max_value = None
    for element in array:
        max_value = max(max_value, element)
    print('Maximum: ', max_value)

    # O(3) complexity
    for i in range(3):
        print('-----------------')


def intersection_count(array1: list[int], array2: list[int]) -> int:
    # O(M * N), M = len(array1), N = len(array2)
    count = 0
    for element1 in array1:
        for element2 in array2:
            if element1 == element2:
                count += 1

    return count


def recursion(index: int, array: list[int]):
    if index == len(array):
        return 0

    branch1 = recursion(index, array)
