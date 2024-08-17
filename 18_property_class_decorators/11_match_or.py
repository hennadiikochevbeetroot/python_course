import random


def get_number_type(natural_less_than_10: int) -> str:
    desc = None
    # if natural_less_than_10 == 3 or natural_less_than_10 == 5 or natural_less_than_10 == 7:
    if natural_less_than_10 in (3, 5, 7):
        desc = 'Prime number'
    elif random.randint(0, 10) < 9:
        desc = 'Random'




def get_number_type(natural_less_than_10: int) -> str:
    desc = None
    match natural_less_than_10:
        case 3 | 5 | 7:
            desc = 'Prime number'
        case natural_less_than_10 if random.randint(0, 10) < 9:
            desc = f'Number is: {natural_less_than_10}'
        case 1:
            desc = 'Exactly one'
        case _:
            desc = 'Other number'

    return desc


print(get_number_type(4))
