import pytest
import sys


@pytest.mark.skip(reason='Skipped for such a reason')
def test_to_skip_with_reason():
    assert len([1, 2, 3]) == 4


@pytest.mark.skipif(sys.version_info < (3, 7), reason='Python must be >= 3.7')
def test_to_skip_if_python_low_version():
    assert 'Stringreplace'.replace('replace', '') == 'String'


@pytest.mark.xfail()
def test_which_is_expected_to_fail():
    assert False


@pytest.mark.xfail()
def test_which_is_expected_to_fail_but_will_work():
    assert True
