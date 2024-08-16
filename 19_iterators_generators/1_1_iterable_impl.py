from collections.abc import Iterable


class OurIterable:
    def __iter__(self):
        # some logic, maybe loop
        yield None


if isinstance(OurIterable(), Iterable):
    print('Our Iterable is Iterable')
