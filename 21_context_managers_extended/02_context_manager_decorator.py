from contextlib import contextmanager


@contextmanager
def file(path: str, mode: str):
    print('Entering file')
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
        print('Closing file')


if __name__ == '__main__':
    file_manager = file('context.txt', 'a')
    with file_manager as f:
        f.write('Hello!\n')
