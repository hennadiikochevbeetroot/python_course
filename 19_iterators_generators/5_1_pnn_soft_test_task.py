# Test task:
# Write a function which takes a string containing brackets
# and checks if each of open brackets are meeting closed one
# Simply talking, check if brackets are correctly placed


def is_brackets_correct(input_brackets: str) -> bool:
    pass


# TESTING ZONE
test_brackets = {
    "()": True,
    "{}": True,
    "[]": True,
    "[()]": True,
    "[({})]": True,
    "[({()})]": True,
    "[({([])})]": True,
    "[({([(){{()()(){}}}])})]": True,
    "[]()[)[)": False,
    "[]()()()[][)[)": False,
    "()([][[[[}}}))": False,
    "[": False,
    "(": False,
    "{": False,
    "{{{": False,
    "{{{{{]}{}{{}{{)))": False,
    "[(])}": False,
    "[(])()()}": False,
    ")(": False,
}
for key, value in test_brackets.items():
    print(f"Test passed {key}: {is_brackets_correct(key) == value}")


