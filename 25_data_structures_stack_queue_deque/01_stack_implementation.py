class Stack:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    @property
    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack> from top to base\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty)
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size)
    print(s.is_empty)
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size)
    print(s)
    print(s.pop())
    print(s)
