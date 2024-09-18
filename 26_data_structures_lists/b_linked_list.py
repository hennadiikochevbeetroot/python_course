from typing import Any
from a_node import Node


class LinkedList:
    def __init__(self):
        self.root: Node | None = None

    @property
    def is_empty(self) -> bool:
        return self.root is None

    def add_left(self, value: Any) -> None:
        self.root = Node(value, self.root)

    def add_right(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value, None)
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = Node(value, None)

    @property
    def size(self) -> int:
        count = 0
        current = self.root
        while current is not None:
            count += 1
            current = current.next

        return count

    def is_present(self, value: Any) -> bool:
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def index(self, value: Any) -> int:
        idx = 0
        current = self.root
        while current is not None:
            if current.value == value:
                return idx

            current = current.next
            idx += 1

        # Not found
        return -1

    def remove(self, value: Any) -> None:
        previous, current = None, self.root
        found = False
        while not found:
            if current.value == value:
                found = True
            else:
                previous, current = current, current.next

        if previous is None:
            self.root = current.next
        else:
            # even if not found, then last element's next would be None
            previous.next = current.next

    def __str__(self) -> str:
        result = 'Linked List: '
        current = self.root
        while current is not None:
            result += f'{current.value} -> '
            current = current.next
        return result + 'NULL(END)'


# TODO: passing list to constructor

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add_left('dog')
    linked_list.add_left(234)
    linked_list.add_left(True)
    linked_list.add_left(45.6)
    linked_list.add_right('rightest')

    print(linked_list)
    print(linked_list.size)
    print(linked_list.is_present(45))

    linked_list.remove(234)
    print(linked_list)
    print(linked_list.index('dog'))
    print(linked_list.index(234))
