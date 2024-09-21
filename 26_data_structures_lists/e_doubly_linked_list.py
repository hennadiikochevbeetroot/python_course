from __future__ import annotations

from typing import Any

class Node:
    def __init__(self, value: Any, prev: Node | None = None, next: Node | None = None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.root: Node | None = None

    # add_right
    def append(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = Node(value, prev=current)

    # add_left
    def prepend(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.prev = Node(value, next=self.root)
            self.root = self.root.prev

    def remove(self, value: Any) -> None:
        if self.root is None:
            return

        current = self.root
        while current is not None:
            if current.value == value:
                # Not first element
                if current.prev is not None:
                    current.prev.next = current.next
                # Not last element
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.root:
                    self.root = current.next
                    self.root.prev = None
                return

            current = current.next

    def print_forward(self):
        print('Doubly Linked List (forward): NULL <- ', end='')
        current = self.root
        while current is not None:
            print(current.value, end=' <-> ' if current.next is not None else ' -> NULL \n')
            current = current.next

    def print_backward(self):
        print('Doubly Linked List (backward): NULL <- ', end='')
        current = self.root
        while current.next is not None:
            current = current.next

        while current is not None:
            print(current.value, end=' <-> ' if current.prev else ' -> NULL \n')
            current = current.prev


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(10)
    doubly_linked_list.prepend(5)
    doubly_linked_list.append(20)
    doubly_linked_list.append(40)
    doubly_linked_list.prepend(1)

    doubly_linked_list.print_forward()
    doubly_linked_list.remove(10)
    #
    doubly_linked_list.print_forward()
    doubly_linked_list.print_backward()
