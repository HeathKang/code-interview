# Pattern: Right-to-left scan
# Time: O(n)
# Space: O(1)
# Mistakes: The first version was correct, but it was missing review notes.


class Solution:
    # Original Code:
    # class Solution:
    #     def romanToInt(self, s: str) -> int:
    #         symbol = {
    #             "I": 1,
    #             "V": 5,
    #             "X": 10,
    #             "L": 50,
    #             "C": 100,
    #             "D": 500,
    #             "M": 1000,
    #         }
    #         res = 0
    #         cur = 0
    #         for i in range(len(s)-1, -1, -1):
    #             if symbol[s[i]] < cur:
    #                 res = res - symbol[s[i]]
    #             else:
    #                 res = res + symbol[s[i]]
    #             cur = max(symbol[s[i]], cur)
    #         return res
    #
    # Key Point:
    # Scan from right to left. A symbol is subtracted only when a larger symbol
    # has already appeared to its right.
    #
    # Better Version:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        max_right = 0
        for ch in reversed(s):
            value = values[ch]
            if value < max_right:
                total -= value
            else:
                total += value
                max_right = value

        return total
