# In PyTest, all test lines are written by pythonic `assert`
# And functions which are considered tests to run, need to start with test_

def test_true():
    assert True


def test_equal_lists():
    assert [1, 2] == [1, 2]


# def test_failing():
#     assert True == False

# def test_failing_lists():
#     assert [1, 2, 3, 4] == [1, 3, 2, 4]
