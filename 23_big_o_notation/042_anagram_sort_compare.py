
# Sorting is usually N^2 or NlogN in best case

# Solution in at least O(NlogN)
def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_list = list(s1)
    s2_list = list(s2)

    # O(NlogN) - Timsort/Powersort
    s1_list.sort()
    # O(NlogN) - Timsort/Powersort
    s2_list.sort()

    pos = 0
    matches = True
    # O(N)
    while pos < len(s1) and matches:
        if s1_list[pos] == s2_list[pos]:
            pos += 1
        else:
            matches = False

    return matches


print(is_anagram('heart', 'earth'))
