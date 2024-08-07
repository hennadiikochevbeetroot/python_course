import time
from getpass import getpass
from functools import wraps

USERS_DB: dict[str, str] = {
    'username': 'password'
}


# TODO: Bonus Task: enhance it to be with parameter - raise_exception: bool

def cli_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = input('Enter your username: ')
        password = getpass('Enter your password: ')
        if USERS_DB.get(username) == password:
            return func(*args, **kwargs)
        else:
            print('Authentication failed')
            return None

    return wrapper


@cli_auth
def send_email(email_to: str, subject: str, message: str) -> bool:
    print(f'Sending email to {email_to} on {subject}: {message[:30]}...')
    time.sleep(2)
    return True


is_email_sent = send_email('test@email.com', 'Final Test', 'Please check my test')
print(is_email_sent)
