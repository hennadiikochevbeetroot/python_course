from collections.abc import Iterable


class OurIterable:
    def __iter__(self):
        return self


class InheritedIterable(Iterable):
    def __iter__(self):
        pass


if isinstance(OurIterable(), Iterable):
    print('Our Iterable is Iterable')

if isinstance(InheritedIterable(), Iterable):
    print('Inheritance also makes it iterable')
