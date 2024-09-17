from typing import Any, Iterable


class Stack:
    def __init__(self, items: Iterable | None = None):
        self.__items = items or []

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, item) -> None:
        self.__items.append(item)

    def pop(self) -> Any:
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    @property
    def size(self):
        return len(self.__items)

    def __repr__(self):
        representation = "<Stack> from top to base\n"
        # for ind, item in enumerate(reversed(self.__items), 1):
        for ind, item in enumerate(self.__items[::-1], 1):
            representation += f"| {str(item)} |\n"

        representation += '--------------\n'
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack([1, 2, 3, 4])
    print(s)

    # print(s.is_empty)
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size)
    # print(s.is_empty)
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size)
    # print(s)
    # print(s.pop())
    # print(s)
