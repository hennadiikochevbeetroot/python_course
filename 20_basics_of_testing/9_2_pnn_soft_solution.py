def is_brackets_correct(input_brackets: str) -> bool:
    opening_brackets = {'(': 0, '[': 0, '{': 0}
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for symbol in input_brackets:
        if symbol in opening_brackets.keys():
            opening_brackets[symbol] += 1
        else:
            opening_brackets[matching_brackets[symbol]] -= 1
            if opening_brackets[matching_brackets[symbol]] < 0:
                return False

    return all(count == 0 for count in opening_brackets.values())


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
