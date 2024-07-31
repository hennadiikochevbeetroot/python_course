import itertools
import random

# INFINITE GENERATORS

c = itertools.count()
# next() function returns next item in the iterator.
# By default starts with number 0 and increments by 1.
print(next(c))  # Output:0
print(next(c))  # Output:1
print(next(c))  # Output:2
print(next(c))  # Output:3

# counter = 0
# while True:
#     counter += 1


for counter in itertools.count():
    print(counter)
    if counter == 100:
        break

l1 = [1, 2, 3]
# using list iterable as an argument in itertools.cycle()
l2 = itertools.cycle(l1)
print(l2)  # Output:<itertools.cycle object at 0x02F794E8>

for element in itertools.cycle(l1):
    if random.random() > 0.9:
        print('Winner ', element)
        break

count = 0
for i in l2:
    # It will end in infinite loop. So have to define terminating condition.
    if count > 15:
        break
    else:
        print(i, end=" ")  # Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
        count += 1

# times argument is not mentioned. It will result in infinite loop.
l1 = itertools.repeat(2)
print(next(l1))  # Output:2
print(next(l1))  # Output:2

# for value in itertools.repeat('some string'):
#     print(value)
#     if


l1 = itertools.chain(["red", "blue"], [1, 2, 3], "hello")
# Returns an iterator object
print(l1)  # Output:<itertools.chain object at 0x029FE4D8>
# converting iterator object to list object
print(list(l1))  # Output:['red', 'blue', 1, 2, 3, 'h', 'e', 'l', 'l', 'o']

l2 = itertools.permutations([3, 2, 1])  # 3! = 1 * 2 * 3 = 6
print(list(l2))  # Output:[(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]
