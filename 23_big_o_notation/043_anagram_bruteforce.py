import itertools


# O(N!) solution - using permutations
def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    all_permutations = itertools.permutations(s1)

    # O(N!)
    for perm in all_permutations:
        if ''.join(perm) == s2:
            return True

    return False


print(is_anagram('heart', 'earth'))
