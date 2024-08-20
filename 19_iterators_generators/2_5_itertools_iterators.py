import itertools
import operator

# create an infinite iterator that starts at 1 and increments by 2 each time
infinite_count = itertools.count(start=1, step=2)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_count))

print('--------------------------------')

# Repeat gives us same objects specified number of times, if not specified, then infinitely
rep = itertools.repeat('value', 5)
for same_value in rep:
    print(same_value)

print('--------------------------------')

# Cartesian product (all combinations from iterables)
list1 = ['key1', 'key2', 'key3']
list2 = ['value1', 'value2', 'value3']

for pair in itertools.product(list1, list2):
    key, value = pair
    print('Combination: ', key, value)

print('--------------------------------')

# Permutations - all possible orders in a list
numbers = [5, 8, 9, 4]
for perm in itertools.permutations(numbers):
    print('Current permutation: ', perm)
    if list(perm) == sorted(numbers):
        print('Permutation above is sorted')

print('--------------------------------')
# Accumulate takes iterable and gets incremental result using given operator
numbers2 = [4, 7, 2, 3]
for intermediate in itertools.accumulate(numbers2, operator.mul):
    print('Multiplying numbers, current result: ', intermediate)

print('--------------------------------')

numbers3 = [2, 4, 5, 7, 8]
is_even = lambda num: num % 2 == 0

# Takewhile takes while function returns true
print('First even numbers: ', end='')
print(list(itertools.takewhile(is_even, numbers3)))


# Dropwhile starts taking values, when given function returns false for first time
print('First non-even number and all next: ', end='')
print(list(itertools.dropwhile(is_even, numbers3)))


# Filterfalse is like filter, but returns only which are false
print('All non-even numbers: ', end='')
print(list(itertools.filterfalse(is_even, numbers3)))

