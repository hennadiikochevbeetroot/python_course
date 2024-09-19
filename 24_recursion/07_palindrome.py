def is_palindrome_iterative(word: str):
    """Return True if word is a palindrome, False if not."""
    # O(N)
    return word == word[::-1]

# racecar
# civic
# hannah
def is_palindrome_recursive(word: str):
    if len(word) <= 1:
        # base case
        return True
    else:
        # check equivalence of first and last char and pass a word without them
        # r == r, a == a, c == c
        # O(N/2) -> O(N)
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])


print(is_palindrome_iterative('racecar'))
print(is_palindrome_recursive('racecar'))

print(is_palindrome_iterative('troglodyte'))
print(is_palindrome_recursive('troglodyte'))
