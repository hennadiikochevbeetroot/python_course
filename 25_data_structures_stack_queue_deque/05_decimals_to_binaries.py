# Algorithm:
# Divide by 2, take remainder and progress until reach 0

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


print(decimal_to_binary(233))


