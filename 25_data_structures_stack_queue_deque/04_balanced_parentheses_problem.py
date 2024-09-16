class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()


def is_balanced(parentheses: str) -> bool:
    stack = Stack()

    balanced = True
    for symbol in parentheses:
        if not balanced:
            break

        if symbol == '(':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()

    # By the end stack be empty
    return balanced and stack.is_empty()


print(is_balanced('(()()()())'))
