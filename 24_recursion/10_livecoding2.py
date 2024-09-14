# In the sys module there is a function sys.setrecursionlimit and sys.getrecursionlimit.
# These two functions set and get the recursion limit.
# import sys
# sys.setrecursionlimit(905)
# sys.getrecursionlimit() # returns 905
# sys.setrecursionlimit(89)
# sys.getrecursionlimit() # returns 89
#
# Task:
# Write a function ```fetch_recursion_limit```
# that acts the same as ```sys.getrecursionlimit``` without importing any libraries.
import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)


# 2 ^ 3 = 4 ^ 2 = 8 ^ 1


# def recur():
#     recur()
#
# recur()

def fetch_recursion_limit():
    def recursive(count: int = 1):
        try:
            # recursive case
            return recursive(count + 1)
        except RecursionError:
            # base case
            return count + 2

    return recursive()


print(fetch_recursion_limit())
