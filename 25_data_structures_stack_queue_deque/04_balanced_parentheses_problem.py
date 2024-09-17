class Stack:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()


def is_balanced(parentheses: str) -> bool:
    stack = Stack()

    balanced = True
    for symbol in parentheses:
        if not balanced:
            break

        if symbol in ['(', '{', '[']:
            stack.push(symbol)
        else:
            if stack.is_empty:
                balanced = False
            else:
                opening = stack.pop()
                if not matches(opening, symbol):
                    balanced = False

    # By the end stack be empty
    return balanced and stack.is_empty


def matches(opening: str, closing: str) -> bool:
    match_brackets = {'{': '}', '[': ']', '(': ')'}
    return match_brackets[opening] == closing


print(is_balanced('(()()()())'))

# Bonus: enhance to handle all brackets
# Tip: needed matches function
# is_balanced('{({([][])}())}') -> True
# is_balanced('[{()]') -> False
# {()} - correct, {(}) - incorrect

print(is_balanced('{({([][])}())}'))
print(is_balanced('[{()]'))
