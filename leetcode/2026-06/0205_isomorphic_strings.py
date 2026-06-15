# Pattern: Bidirectional hash map
# Time: O(n)
# Space: O(k), where k is the number of distinct mapped characters
# Mistakes: The first version was correct, but checking `t[i] in d.values()`
# can make the scan O(n^2) because dictionary values are not indexed.


class Solution:
    # Original Code:
    # class Solution:
    #     def isIsomorphic(self, s: str, t: str) -> bool:
    #         d = {}
    #
    #         for i in range(len(s)):
    #             if s[i] in d:
    #                 if d[s[i]] != t[i]:
    #                     return False
    #             else:
    #                 if t[i] in d.values():
    #                     return False
    #                 d[s[i]] = t[i]
    #
    #         return True
    #
    # Key Point:
    # Each character in `s` must map to exactly one character in `t`, and each
    # character in `t` can be used by only one character from `s`.
    #
    # Better Version:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for s_char, t_char in zip(s, t):
            if s_char in s_to_t and s_to_t[s_char] != t_char:
                return False
            if t_char in t_to_s and t_to_s[t_char] != s_char:
                return False

            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char

        return True
