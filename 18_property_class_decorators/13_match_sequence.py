def match_string(input_str: str):
    match input_str[0]:
        case 'h':
            print('First char is h')
        case 'H':
            print('First char is capital H')


match_string('Hello')


def match_list(lst: list):
    match lst:
        case ['a']:
            print('Only one element a')
        case ['a', *other]:
            print(f'First element a, other are: {other}')
        case [*prev, 'a']:
            print(f'Last element a, previous are: {prev}')
        case _:
            print('Other case')


match_list(['b', 'c', 'a'])


def match_dict(dct: dict):
    match dct:
        case {'key': value}:
            print('Key name is key, value:', value)
        case {'key1': value1, 'key2': value2}:
            print(f'Value1 = {value1}, value2={value2}')
        case _:
            print('Unhandled case')


match_dict({'key1': 2, 'key2': 'some_string'})
