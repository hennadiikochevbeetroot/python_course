# These convert to False
empty_string = ''
zero_int = 0
zero_float = 0.0
empty_list = []
empty_set = set()
empty_dict = dict()
empty_tuple = tuple()
none = None

# These convert to True
non_empty_string = 'aaaaaaa'
not_zero = 12345
list_with_at_least_one_element = [1]
set_with_at_least_one_element = {2}
dict_with_at_least_one_pair = {3: 4}
tuple_with_at_least_one_element = (1,)


# Example:
if non_empty_string:
    print('Hello')
