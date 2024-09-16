class Deque:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return self.size == 0

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    @property
    def size(self):
        return len(self._items)


def is_palindrome(word: str) -> bool:
    deque = Deque()
    for char in word:
        deque.add_rear(char)

    still_palindrome = True
    # If only one char left in deque,
    # then it is still symmetric
    while deque.size > 1 and still_palindrome:
        first_char = deque.remove_rear()
        last_char = deque.remove_front()
        if first_char != last_char:
            still_palindrome = False

    return still_palindrome


print(is_palindrome('radare'))


