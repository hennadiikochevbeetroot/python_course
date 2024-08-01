# Functionality of Phonebook CLI application:
#
# 0. An option to exit the program
# 1. Add new entries
# 9. Print contents of dictionary
#
# BELOW IS YOUR HOMEWORK - GIVE IT A TRY
# Bonus: try to split this program into separate files and modules
# separate files for constants, business logic, etc
#
# Search by first name
# Search by last name
# Search by telephone number
# Search by city or country
# Delete a record for a given telephone number
# Update a record for a given telephone number
#
# This program should operate on the console.
# It should display all the choices of available
# commands when the program loads.
#
# Key points:
# 1. all program logic should be split to different functions;
# 2. store all entries in the dict, where
# key is the full name (tuple with length 2 - first name, last name)
# and value another tuple with (all other data):
# {
#     ('John', 'Smith'): ('+12423535', 'Minnesota', 'US')
# }

from typing import Callable

HELP_MESSAGE = """
Welcome to PhoneBook.
Options:
0. An option to exit the program
1. Add new entries
9. Print contents of dictionary
"""

POSSIBLE_OPTIONS = (0, 1, 9)

Phonebook = dict[tuple[str, str], tuple[str, str, str]]


def exit_program() -> None:
    quit(0)


def add_entry(phonebook: Phonebook) -> None:
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone = input('Enter phone: ')
    city = input('Enter city: ')
    country = input('Enter country: ')

    key = (first_name, last_name)
    value = (phone, city, country)
    phonebook[key] = value


def print_phonebook(phonebook: Phonebook) -> None:
    for (first_name, last_name), (phone, city, country) in phonebook.items():
        print(f'Fullname: {first_name} {last_name}; Place: {city} {country}; Phone {phone}')


OPTION_TO_FUNCTION: dict[int, Callable] = {
    1: add_entry,
    9: print_phonebook,
}


def validate_option(user_input: str) -> tuple[bool, int | None]:
    user_input = user_input.strip()
    is_valid = user_input.isdigit() and int(user_input) in POSSIBLE_OPTIONS
    option = int(user_input) if is_valid else None

    return is_valid, option


def phonebook_app() -> None:
    print(HELP_MESSAGE)
    phonebook: Phonebook = {}
    while True:
        user_input = input('Choose an option: ')
        is_valid, option = validate_option(user_input)
        if not is_valid:
            possible_options = ', '.join([str(option) for option in POSSIBLE_OPTIONS])
            print(f'Incorrect option, possible are: {possible_options}')
            continue

        if option == 0:
            quit(option)

        OPTION_TO_FUNCTION[option](phonebook)


if __name__ == '__main__':
    phonebook_app()
