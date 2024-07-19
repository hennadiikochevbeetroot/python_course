user_string = input('Enter your string: ')
if user_string.startswith('hello'):
    print('Hello to you too!')
elif user_string.isdigit():
    user_number = int(user_string)
    print('You have entered a number!')
    print(f'Square root of your number: {user_number ** 0.5}')
else:
    print(f'You typed this: {user_string}')
