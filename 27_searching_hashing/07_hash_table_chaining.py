from typing import Any, Hashable
from dataclasses import dataclass


@dataclass
class Pair:
    key: Hashable
    value: Any


class HashTable:
    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        # Chaining - same hash keys are going to be at same list (could be linked list too)
        self.table: list[list[Pair]] = [[] for _ in range(self.max_size)]

    def hash(self, key: Hashable):
        return hash(key) % self.max_size

    # O(1) - insert best and average, search worst case - O(N) if bad hash function
    def insert(self, key: Hashable, value: Any) -> None:
        hash = self.hash(key)
        for pair in self.table[hash]:
            if pair.key == key:
                # Found key - update
                pair.value = value
                return
        # New key - add
        self.table[hash].append(Pair(key, value))

    # O(1) - best and average, worst - O(N) if bad hash function
    def lookup(self, key: Hashable) -> Any:
        hash = self.hash(key)
        # self.table[hash] - N
        # O(N)
        # self.table[hash] - 0, 1, 2
        # O(C) -> O(1)
        for pair in self.table[hash]:
            if pair.key == key:
                return pair.value

    def pop(self, key: Hashable) -> Any:
        hash = self.hash(key)
        for idx, pair in enumerate(self.table[hash]):
            if pair.key == key:
                value = pair.value
                del self.table[hash][idx]
                return value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.insert(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        return self.lookup(key)

    def __str__(self):
        result = 'Hash Table: {'
        pairs_set = set()
        for slot in self.table:
            pairs = ', '.join(f'{pair.key} : {pair.value}' for pair in slot)
            if pairs:
                pairs_set.add(pairs)

        return result + ', '.join(pairs_set) + '}'


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table['apple'] = 100
    hash_table['banana'] = 200
    hash_table['orange'] = 300

    print(hash_table['banana'])
    print(hash_table.pop('banana'))
    print(hash_table)
