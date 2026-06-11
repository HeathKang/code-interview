# Pattern: Sliding window with last seen index
# Time: O(n)
# Space: O(min(n, charset))
# Mistakes: The first version kept the current window as a list, so membership
# checks and `pop(0)` made the window updates O(n) each in the worst case.


class Solution:
    # Original Code:
    # class Solution:
    #     def lengthOfLongestSubstring(self, s: str) -> int:
    #         if len(s) == 0:
    #             return 0
    #         res = []
    #         left = 0
    #         best = 1
    #         for right, v in enumerate(s):
    #             if v in res:
    #                 while v in res:
    #                     best = max(best, right-left)
    #                     left = left + 1
    #                     res.pop(0)
    #             else:
    #                 best = max(best, right-left+1)
    #             res.append(v)
    #
    #         return best
    #
    # Key Point:
    # Keep `left` after the most recent duplicate. If a character was last
    # seen inside the current window, jump `left` past its previous index.
    #
    # Better Version:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            best = max(best, right - left + 1)

        return best
