from collections.abc import Iterator


class OurIterator(Iterator):

    def __next__(self):
        # some logic
        raise StopIteration

    def __iter__(self):
        return self


# if isinstance(OurIterator(), Iterator):
#     print('Our Iterator is Iterator')
# it = OurIterator()
# it = iter(it)
# for _ in it:
#     print('something')


class ListIterator:
    def __init__(self, collection):
        self.collection = collection
        self.cursor = -1

    def __next__(self):
        if self.cursor + 1 >= len(self.collection):
            raise StopIteration

        self.cursor += 1
        return self.collection[self.cursor]

    def __iter__(self):
        return self


if isinstance(ListIterator([]), Iterator):
    print('List Iterator is Iterator')

list_iterator = ListIterator([1, 2, 3, 4, 5])

# it = iter(list_iterator)
# print(next(it))
# print(next(it))

for number in list_iterator:
    print(number)

print('----------------')
for number in list_iterator:
    print(number)


