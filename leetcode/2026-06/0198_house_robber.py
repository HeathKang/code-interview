# Pattern: Constant-space DP
# Time: O(n)
# Space: O(1)
# Mistakes: The first version had the correct recurrence, but `m.get(n)` misses
# cached zero values and only the previous two states are needed.

from __future__ import annotations

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def rob(self, nums: List[int]) -> int:
    #         m = {}
    #         def dp(n) -> int:
    #             # Use key lookup instead of m.get(n), because a cached 0 is
    #             # falsy but still a valid memoized answer.
    #             if n in m:
    #                 return m[n]
    #
    #             if n == 0:
    #                 m[0] = nums[0]
    #                 return m[0]
    #             if n == 1:
    #                 m[1] = max(nums[0], nums[1])
    #                 return m[1]
    #
    #             m[n] = max(dp(n-1), dp(n-2) + nums[n])
    #             return m[n]
    #
    #         return dp(len(nums)-1)
    #
    # Key Point:
    # For each house, choose the better result between skipping it or robbing it
    # with the best total from two houses back.
    #
    # Better Version:
    def rob(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0

        for money in nums:
            current = max(one_back, two_back + money)
            two_back = one_back
            one_back = current

        return one_back
