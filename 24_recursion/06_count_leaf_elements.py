from typing import Any


def count_leaf_items(item_list: list[Any]):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    count = 0
    for item in item_list:
        count += 1 if type(item) is not list else count_leaf_items(item)
        # if isinstance(item, list):
        #     count += count_leaf_items(item)
        # else:
        #     count += 1

    return count


names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(count_leaf_items(names))
