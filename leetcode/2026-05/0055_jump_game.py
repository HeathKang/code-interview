# Pattern: Greedy / farthest reachable index
# Time: O(n)
# Space: O(1)
# Mistakes: The first attempt added an unnecessary pre-check and made the invariant less clear.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def canJump(self, nums: List[int]) -> bool:
    #         if 0 not in nums:
    #             return True
    #         reach = 0
    #         for i, step in enumerate(nums):
    #             if reach >= i:
    #                 reach = max(reach, i + step)
    #             else:
    #                 return False
    #         return True
    #
    # Key Point:
    # Track the farthest index reachable so far. If the current index is beyond
    # that reach, the path is impossible.
    #
    # Better Version:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0

        for i, step in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + step)

        return True
