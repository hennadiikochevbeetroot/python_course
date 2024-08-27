import pytest


@pytest.fixture
def dictionary_for_test():
    return {'key1': 'value1'}


def test_fixture(dictionary_for_test):
    assert type(dictionary_for_test) is dict
