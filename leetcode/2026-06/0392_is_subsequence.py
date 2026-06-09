# Pattern: Two pointers
# Time: O(n)
# Space: O(1)
# Mistakes: The first version was correct, but it used extra edge-case checks
# instead of letting the pointer invariant handle them.


class Solution:
    # Original Code:
    # class Solution:
    #     def isSubsequence(self, s: str, t: str) -> bool:
    #         if len(t) < len(s):
    #             return False
    #         if len(s) == 0:
    #             return True
    #         cur1 = 0
    #         cur2 = 0
    #         while cur2 < len(t):
    #             if t[cur2] == s[cur1]:
    #                 cur1 = cur1 + 1
    #
    #             cur2 = cur2 + 1
    #             if cur1 == len(s):
    #                 return True
    #
    #         return False
    #
    # Key Point:
    # Keep one pointer on `s`. Scan `t` left to right and advance the pointer
    # only when the current `t` character matches the next needed `s` character.
    #
    # Better Version:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
