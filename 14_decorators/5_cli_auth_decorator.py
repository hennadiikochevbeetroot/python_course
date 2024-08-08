import time
from getpass import getpass
from functools import wraps
from typing import Callable

USERS_DB: dict[str, str] = {
    'username': 'password'
}


# TODO: Bonus Task: enhance it to be with parameter - raise_exception: bool

# def cli_auth(func: Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         username = input('Enter your username: ')
#         password = getpass('Enter your password: ')
#         if USERS_DB.get(username) == password:
#             return func(*args, **kwargs)
#         else:
#             print('Authentication failed')
#             raise Exception('Authentication failed')
#
#     return wrapper


def cli_auth(raise_exception: bool = False):
    def decorator(func: Callable) -> Callable:
        def check_password(username: str, password: str) -> bool:
            return USERS_DB.get(username) == password

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{func.__name__} called with {args}, {kwargs}')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if check_password(username, password):
                return func(*args, **kwargs)
            elif raise_exception:
                raise Exception('Authentication failed')
            else:
                print('Authentication failed without exception')

        return wrapper

    return decorator


@cli_auth(raise_exception=True)
def send_email(email_to: str, subject: str, message: str) -> bool:
    print(f'Sending email to {email_to} on {subject}: {message[:30]}...')
    time.sleep(2)
    return True


is_email_sent = send_email('test@email.com', 'Final Test', message='Please check my test')
print(is_email_sent)
