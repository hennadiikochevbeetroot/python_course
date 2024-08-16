def get_number_explanation_conditions(number: int) -> str:
    description = None
    if number == 666:
        description = 'Devil number'
    elif number == 42:
        description = 'Answer for everything'
    elif number == 7:
        description = 'Prime number'
    else:
        description = 'Just a number'

    return f'Number {number} is {description}'


# Introducted in Python 3.10
def get_number_explanation_match(number: int) -> str:
    description = None
    match number:
        case 666:
            description = 'Devil number'
        case 42:
            description = 'Answer for everything'
        case 7:
            description = 'Prime number'
        case _:
            description = 'Just a number'

    return f'Number {number} is {description}'


if __name__ == '__main__':
    number = int(input('Please enter a number: '))
    print(get_number_explanation_match(number))
