from typing import Any, Hashable

# __hash__

# Hash Table has 3 basic terms:
# 1. Hash function (modulo function is simplest)
# 2. Collisions - here solved with open addressing
# Open addressing is recalculating hash until we reach an empty slot
# 3. Buckets - storage for keys and values


class HashTable:
    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        self.current_size = 0
        self.keys = [None] * self.max_size  # Bucket for keys
        self.values = [None] * self.max_size  # Bucket for values

    def hash(self, key: Hashable) -> int:
        # Most primitive hash function:
        # simply take remainder of division
        return hash(key) % self.max_size

    def rehash(self, hash: int) -> int:
        # Open addressing collision resolve
        # Most primitive - change position to next closest - plus 1
        return (hash + 1) % self.max_size

    def insert(self, key: Hashable, value: Any) -> None:
        if self.current_size >= self.max_size:
            raise ValueError('Hash Table is full')

        hash = self.hash(key)
        # New key - create
        # O(1)
        if self.keys[hash] is None:
            self.keys[hash], self.values[hash] = key, value
        # Existing key - update
        elif self.keys[hash] == key:
            self.values[hash] = value
        # Found key, but not needed one - rehash
        else:
            # O(N)
            while self.keys[hash] is not None and self.keys[hash] != key:
                hash = self.rehash(hash)

            if self.keys[hash] is None:
                # Found empty slot - insert
                self.keys[hash], self.values[hash] = key, value
            else:
                # Found existing key - update
                self.values[hash] = value

        self.current_size += 1

    def lookup(self, key: Hashable) -> Any:
        # 1, 2, 3, 1, 2, 3, 1
        first_hash = self.hash(key)
        hash = first_hash
        while self.keys[hash] is not None:
            # O(1)
            if self.keys[hash] == key:
                return self.values[hash]
            else:
                # O(N)
                hash = self.rehash(hash)
                if hash == first_hash:
                    # Edge case where we checked all previous hashes
                    return None

        return None

    def pop(self, key: Hashable) -> None:
        first_hash = self.hash(key)
        hash = first_hash
        while self.keys[hash] is not None:
            if self.keys[hash] == key:
                self.keys[hash], self.values[hash] = None, None
            else:
                hash = self.rehash(hash)
                if hash == first_hash:
                    return None

    def __setitem__(self, key: Hashable, value: Any) -> None:
        # d[1] = 2
        self.insert(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        # d[1]
        return self.lookup(key)

    def __str__(self):
        result = 'HashTable: {'
        for idx in range(self.max_size):
            if self.keys[idx] is not None:
                result += f'{self.keys[idx]}: {self.values[idx]}, '

        return result + '}'


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table['key1'] = 'value1'
    hash_table['key2'] = 2

    print(hash_table['key2'])

    hash_table['key2'] = 'value2'
    print(hash_table['key2'])

    print(hash_table)
    hash_table.pop('key1')
    print(hash_table)
