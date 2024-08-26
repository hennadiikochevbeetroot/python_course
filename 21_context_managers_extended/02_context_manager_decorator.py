from contextlib import contextmanager


@contextmanager
def file(path: str, mode: str):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    with file('context.txt', 'a') as f:
        f.write('Hello!\n')
