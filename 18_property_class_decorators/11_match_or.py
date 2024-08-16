

def get_number_type(natural_less_than_10: int) -> str:
    desc = None
    match natural_less_than_10:
        case 3 | 5 | 7:
            desc = 'Prime number'
        case 2 | 4 | 6 | 8 as even_number:
            desc = f'Number is: {even_number}'
        case 1:
            desc = 'Exactly one'
        case _:
            desc = 'Other number'

    return desc


print(get_number_type(4))
