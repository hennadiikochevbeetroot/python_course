import random


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    @property
    def size(self):
        return len(self._items)


def hot_potato_game(names: list[str]):
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size > 1:
        for switch in range(random.randint(3, 6)):
            # Put each next child to be last
            child = queue.dequeue()
            print(f'{child} gave potato to next one')
            queue.enqueue(child)

        round_lost = queue.dequeue()
        print(f'Child with potato: {round_lost} and he/she leaves the game')

    winner = queue.dequeue()
    print('And our winner is: ', winner)


children = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
hot_potato_game(children)
