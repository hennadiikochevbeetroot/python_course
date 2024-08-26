# Let's see how would file context manager
# look like

from types import TracebackType
from typing import Type


class File:
    def __init__(self, path: str, mode: str):
        self.file = open(path, mode)

    def __enter__(self):
        print('Entering file')
        return self.file

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> bool:
        print('Closing file')
        self.file.close()

        if exc_type:
            print(f'Exception {exc_type} {exc_val} {exc_tb} is suppressed')

        return True  # If returns anything but True, when exception is re-raised


if __name__ == '__main__':
    with File('context.txt', 'a') as file:
        file.write('Hello!\n')
