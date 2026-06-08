from typing import List


# Pattern: Top-down DP
# Time: O(n^2)
# Space: O(n)
# Mistakes: The first version computed the best subsequence ending at `n`,
# but returned only the state for the last index and left some states as -1.


class Solution:
    # Original Code:
    # class Solution:
    #     def lengthOfLIS(self, nums: List[int]) -> int:
    #         mem = {}
    #         mem = {k:-1 for k in range(len(nums))}
    #         def dp(n) -> int:
    #             if n in mem and mem[n] != -1:
    #                 return mem[n]
    #
    #             if n == 0:
    #                 mem[0] = 1
    #                 return 1
    #
    #             for i in range(n):
    #                 if nums[n] > nums[i]:
    #                     if n in mem:
    #                         mem[n] = max(mem[n], dp(i) + 1)
    #                     else:
    #                         mem[n] = dp(i) + 1
    #             return mem[n]
    #
    #         return dp(len(nums)-1)
    #
    # Key Point:
    # State: `dp(i)` is the LIS length ending exactly at index `i`.
    # Transition: for every `j < i`, if `nums[j] < nums[i]`, then `nums[i]`
    # can extend the subsequence ending at `j`: `dp(i) = max(dp(i), dp(j) + 1)`.
    # Base cases: every element is a length-1 subsequence by itself.
    # Memo: cache each `dp(i)` so every ending index is solved once.
    # Answer: return `max(dp(i))`, because the LIS can end at any index.
    #
    # Better Version:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i: int) -> int:
            if i in memo:
                return memo[i]

            best = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, dp(j) + 1)

            memo[i] = best
            return best

        return max(dp(i) for i in range(len(nums)))
