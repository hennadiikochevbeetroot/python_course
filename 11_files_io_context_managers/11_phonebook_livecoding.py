# Functionality of Phonebook application:
#
# 0. An option to exit the program
# 1. Add new entries
# 9. Print contents of dictionary
# Search by first name
# Search by last name
# Search by last name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number

# This program should operate on the console.
# It should display all the choices of available
# commands when the program loads.


# Key points:
# 1. all program logic should be split to different functions;
#
# 2. store all entries in the dict, where
# key is the full name (tuple with length 2 - first name, last name)
# and value another tuple with (all other data);
# {
#     ('John', 'Smith'): ('+12423535', 'Minnesota', 'US')
# }

HELP_MESSAGE = """
Welcome to PhoneBook.
Options:
0. An option to exit the program
1. Add new entries
9. Print contents of dictionary
"""

POSSIBLE_OPTIONS = (0, 1, 9)


def validate_option(user_input: str) -> tuple[bool, int | None]:
    user_input = user_input.strip()
    is_valid = user_input.isdigit() and int(user_input) in POSSIBLE_OPTIONS
    option = int(user_input) if is_valid else None

    return is_valid, option


def phonebook_app() -> None:
    print(HELP_MESSAGE)
    while True:
        user_input = input('Choose an option: ')
        is_valid, option = validate_option(user_input)
        if not is_valid:
            possible_options = ', '.join([str(option) for option in POSSIBLE_OPTIONS])
            print(f'Incorrect option, possible are: {possible_options}')
            continue

        print('Correct option.')


if __name__ == '__main__':
    phonebook_app()
