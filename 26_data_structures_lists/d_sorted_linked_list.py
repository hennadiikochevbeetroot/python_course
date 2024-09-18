from a_node import Node

Number = int | float


# Could be called Ordered Linked List
# (in comparison to previous Unordered)
class SortedLinkedList:
    def __init__(self):
        self.root: Node | None = None

    @property
    def is_empty(self) -> bool:
        return self.root is None

    @property
    def size(self) -> int:
        count = 0
        current = self.root
        while current is not None:
            count += 1
            current = current.next

        return count

    def is_present(self, value: Number) -> bool:
        current: Node | None = self.root
        while current is not None:
            if current.value == value:
                return True
            if current.value > value:
                return False

            current = current.next

        return False

    def add(self, value: Number) -> None:
        previous, current = None, self.root
        while current is not None:
            if current.value > value:
                break
            previous, current = current, current.next

        if previous is None:
            self.root = Node(value, self.root)
        else:
            previous.next = Node(value, current)

    def remove(self, value: Number) -> None:
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

    def __str__(self):
        result = 'Sorted Linked List: '
        current = self.root
        while current is not None:
            result += f'{current.value} -> '
            current = current.next
        return result + 'NULL(END)'


if __name__ == "__main__":
    sorted_linked_list = SortedLinkedList()
    sorted_linked_list.add(31)
    sorted_linked_list.add(77)
    sorted_linked_list.add(17)
    sorted_linked_list.add(93)
    sorted_linked_list.add(26)
    sorted_linked_list.add(54)

    print(sorted_linked_list)
    print(sorted_linked_list.size)

    print(sorted_linked_list.is_present(77))
    print(sorted_linked_list.is_present(555))

    sorted_linked_list.remove(31)
    print(sorted_linked_list)
