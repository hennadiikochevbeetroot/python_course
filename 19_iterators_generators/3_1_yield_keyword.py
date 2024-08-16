


def yield_multiple_statements():
    yield "This is the first statement"
    yield "This is the second statement"
    yield "This is the third statement"


generator = yield_multiple_statements()
print(next(generator))
print(next(generator))
print(next(generator))

# if we try to continue calling next(),
# program will raise StopIteration exception

print(next(generator))

