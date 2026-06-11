from typing import List


# Pattern: Sliding window
# Time: O(n)
# Space: O(1)
# Mistakes: The first version repeatedly recomputed sums and chose which side
# to shrink by endpoint value, but the minimum window depends on the running
# sum, not on which endpoint is larger.


class Solution:
    # Original Code:
    # class Solution:
    #     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #         res = []
    #         left = 0
    #         right = len(nums)
    #         if sum(nums) < target:
    #             return 0
    #         while True:
    #             if sum(nums[left:right]) >= target:
    #                 if nums[left] > nums[right-1]:
    #                     if sum(nums[left:right-1]) >= target:
    #                         right = right - 1
    #                     else:
    #                         break
    #                 else:
    #                     if sum(nums[left+1:right]) >= target:
    #                         left = left + 1
    #                     else:
    #                         break
    #
    #         return right-left
    #
    # Key Point:
    # Expand `right` until the window sum reaches `target`, then shrink `left`
    # while the window is still valid. Because all numbers are positive,
    # shrinking can only decrease the sum, so each index moves at most once.
    #
    # Better Version:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = len(nums) + 1

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == len(nums) + 1 else best
