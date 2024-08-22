# Pytest test classes must start with Test

# To run specific test method, syntax:
# pytest file_path.py::TestClassName::test_method_name

class TestGroup:

    def test_something(self):
        assert 2 + 2 == 4

    def test_other_thing(self):
        assert len('qwerty') == 6
