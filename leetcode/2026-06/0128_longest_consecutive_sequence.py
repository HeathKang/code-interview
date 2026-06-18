from typing import List


# Pattern: Hash map sequence starts
# Time: O(n)
# Space: O(n)


class Solution:
    # Original Code:
    # No prior attempt in this repository.
    #
    # Key Point:
    # Put every number in a dictionary key. A number can start a consecutive
    # sequence only when `num - 1` is absent, so each sequence is counted once
    # from its first value instead of restarting from every element.
    #
    # Better Version:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = {}
        for num in nums:
            values[num] = True

        best = 0

        for num in values:
            if num - 1 in values:
                continue

            current = num
            length = 1
            while current + 1 in values:
                current += 1
                length += 1

            best = max(best, length)

        return best
