def match_string(input_str: str):
    match len(input_str):
        # Puts len value into inter
        case inter if len(input_str) > 5:
            # print('First char is h')
            print(f'Length is greater than 5, value={inter}')
        case _:
            # print('First char is capital H')
            print('Length is less or equal to 5')


# match_string('Hellostring')


def match_list(lst: list):
    match lst:
        case ['a']:
            print('Only one element a')
        case ['a', *other]:
            others = ', '.join([str(el) for el in other])
            print(f'First element a, other are: ', others)
        case [*prev, 'a', 'c'] as result:
            print(f'Whole list: {result}, previous are: {prev}')
        case _:
            print('Other case')

    return None


# match_list(['a', 'b', 'a', 'c'])


_ = 2  # Possible name for a variable
print(_)


def match_dict(dct: dict):
    match dct:
        case {'a': 'b', 'c': 'd'}:
            print("Dictionary is exactly {'a': 'b'}")
        # case {key: value}: # Impossible
        #     print('')
        case {'key': value}:
            print('Key name is key, value:', value)
        # case {'key1': value1, 'key2': value2}:
        #     print(f'Value1 = {value1}, value2 = {value2}')
        case {'key1': _, 'key2': _}:  # Cannot print _ contents
            print('Key1, and 2 inside of dict only')
        case _:
            print('Unhandled case')


match_dict({'key1': 2, 'key2': 'some_string'})
