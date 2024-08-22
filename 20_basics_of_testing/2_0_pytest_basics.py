# In PyTest, all test lines are written by pythonic `assert`
# And functions which are considered tests to run, need to start with test_
import pytest


# Run options:
# specify one or more files, or whole directory
# file_name::function_name for running specific function
# -v for more output
# -q for less output
# -k filter by test names
# -m filter by markers
# --collect-only  check tests which are going to be run (dry-run)
# -x exit on first error
# --maxfail maximum allowed fails
# --last-failed re-run only those tests which failed last time
# --failed-first run all tests, but first run those which failed last time


# @pytest.mark.run_this_time
def test_true():
    assert True


def test_one():
    # assert False
    assert 1 > 0


# @pytest.mark.run_this_time
def test_equal_lists():
    assert [1, 2] == [1, 2]

# def test_failing():
#     assert True == False

# def test_failing_lists():
#     assert [1, 2, 3, 4] == [1, 3, 2, 4]
