from typing import List


# Original Code
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums_new = nums.copy()
#         step = len(nums) - k % len(nums)
#         for i in range(len(nums)):
#             if i + step < len(nums):
#                 nums[i] = nums_new[i+step]
#             else:
#                 nums[i] = nums_new[i+step-len(nums)]
#
# Key Point
# Rotate right by `k` using three reversals:
# - Reverse the whole array.
# - Reverse the first `k` elements.
# - Reverse the remaining elements.
# Normalize `k` with `k %= len(nums)` because rotating by the array length
# returns the original order.


# Better Version
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if not nums:
            return

        k %= len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
