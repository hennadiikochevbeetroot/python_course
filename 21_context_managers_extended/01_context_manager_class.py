# Let's see how would file context manager
# look like

from types import TracebackType
from typing import Type


# with open() as file:
#     file.write()

# with File('path.txt', 'w')

class File:
    def __init__(self, path: str, mode: str):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)

    def __enter__(self):
        print('Entering file')
        return self.file

    # self.__exit__(ZeroDivisionError, ZeroDivisionError('message'))
    # Exception

    def __exit__(
            self,
            exc_type: Type[Exception] | None,
            exc_val: Exception | None,
            exc_tb: TracebackType | None
    ):
        print('Closing file')
        self.file.close()

        if exc_type is not None:
            print(f'Exception {exc_type.__name__} {exc_val} {exc_tb} is suppressed')

        # If returns anything but True, when exception is re-raised
        return False


if __name__ == '__main__':
    file = File('context.txt', 'a')    # __init__ call
    with file as f:                              # __enter__ call
        a = 5 / 0
        f.write('Hello!\n')

    # __exit__ call
    print('Overcome error')
