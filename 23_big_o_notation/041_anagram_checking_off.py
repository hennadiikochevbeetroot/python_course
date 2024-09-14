# heart - earth
# [None,None,a,r,t]   [None,a,r,t,None]


# O(N^2) solution
def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s2_list = list(s2)
    pos1 = 0

    still_ok = True
    # O(N^2 / 2) -> O(N^2)
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2_list) and not found:
            if s1[pos1] == s2_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            s2_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


print(is_anagram('heart', 'earth'))
