def square_user_inputs():
    while True:
        number = yield
        yield number ** 2


gen = square_user_inputs()
for _ in range(2):
    number = int(input('Enter a number: '))
    next(gen)
    result = gen.send(number)
    print('Squared: ', result)
