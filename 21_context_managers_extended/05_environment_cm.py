import os
from contextlib import contextmanager


@contextmanager
def temp_environment(**envs):
    """Temporarily set environment variables inside the context … """

    # Save old vars and replace them with new ones
    original_env = {env: os.environ.get(env) for env in envs}
    os.environ.update(envs)

    try:
        yield  # Simply start what's inside of CM block
    finally:
        # Return old env vars back
        for k, v in original_env.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v


if __name__ == '__main__':
    print('Current domain is: ', os.environ.get('USERDOMAIN'))

    with temp_environment(USERDOMAIN='NEWDOMAINTEMPORARY'):
        print('Inside temporary: ', os.environ.get('USERDOMAIN'))

    print('Back outside: ', os.environ.get('USERDOMAIN'))
