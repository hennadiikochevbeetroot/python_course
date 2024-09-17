# Algorithm:
# Divide by 2, take remainder and progress until reach 0
# 234(10) = 2 * 10^2 + 3 * 10^1 + 4 * 10^0
# 101(2) = 1 * 2^2 + 1 * 2^1 + 1 * 2^0 = 5

# 5 // 2 = 2, remainder 1, push
# 2 // 2 = 1, remainder 0, push
# 1 // 2 = 0, remainder 1, push

# 34 // 2 = 17, 0
# 17 // 2 = 8, 1
# 8 // 2 = 4, 0
# 4 // 2 = 2, 0
# 2 // 2 = 1, 0
# 1 // 2 = 0, 1
# Result: 100010


class Stack:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()


def decimal_to_binary(decimal: int) -> str:
    stack = Stack()
    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal //= 2

    binary = ''
    while not stack.is_empty:
        binary += str(stack.pop())

    return binary


print(decimal_to_binary(34))
