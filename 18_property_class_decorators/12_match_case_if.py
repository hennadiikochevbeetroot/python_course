def match_number(number: int, printing: str = True):
    match number:
        case 1 if printing:
            print(f'Number {number} is exactly 1')
        case 0 if not printing:
            print('0 without printing')
        case _:
            print('Something else')


match_number(1)
