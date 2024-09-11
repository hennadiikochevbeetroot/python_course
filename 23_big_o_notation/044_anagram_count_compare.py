# O(N) solution

ALPHABET_SIZE = 26


def is_anagram(s1: str, s2: str) -> bool:
    count1 = [0] * ALPHABET_SIZE
    count2 = [0] * ALPHABET_SIZE

    # O(N)
    for letter in s1:
        # ASCII Table code difference (max 25)
        # ord('a') == 97
        # ord('z') == 122
        pos = ord(letter) - ord('a')
        count1[pos] += 1

    # O(N)
    for letter in s2:
        pos = ord(letter) - ord('a')
        count2[pos] += 1

    idx = 0
    still_ok = True
    # O(N) worst case
    while idx < ALPHABET_SIZE and still_ok:
        if count1[idx] == count2[idx]:
            idx += 1
        else:
            still_ok = False

    return still_ok


print(is_anagram('apple', 'pleap'))
