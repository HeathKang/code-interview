# Pattern: Character counting
# Time: O(n + m)
# Space: O(k), where k is the number of distinct characters in `ransomNote`
# Mistakes: The first version was correct, but it created an unused dictionary
# and shadowed that variable while scanning `magazine`.


class Solution:
    # Original Code:
    # class Solution:
    #     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #         r = {}
    #         m = {}
    #         for l in ransomNote:
    #             if l in r:
    #                 r[l] = r[l] + 1
    #             else:
    #                 r[l] = 1
    #         for m in magazine:
    #             if m in r:
    #                 r[m] = r[m] - 1
    #
    #         for k in r:
    #             if r[k] > 0:
    #                 return False
    #
    #         return True
    #
    # Key Point:
    # Count the characters still needed from `ransomNote`. Each matching
    # magazine character pays down that need, and all counts must reach zero.
    #
    # Better Version:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        needed = {}

        for char in ransomNote:
            needed[char] = needed.get(char, 0) + 1

        for char in magazine:
            if char in needed:
                needed[char] -= 1

        for count in needed.values():
            if count > 0:
                return False

        return True
