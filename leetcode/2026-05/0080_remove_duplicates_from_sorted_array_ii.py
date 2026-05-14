from typing import List


# Original Code
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # two pointer
#         if len(nums) <= 2:
#             return len(nums)
#
#         left = 0
#         right = 0
#         while right < len(nums):
#             if left < 2 or nums[right] != nums[left - 2]:
#                 nums[left] = nums[right]
#                 left = left + 1
#             right = right + 1
#
#         return left
#
# Key Point
# Separate the two pointers by responsibility:
# - `read` only scans the original array from left to right.
# - `write` only extends the valid answer prefix.
# This avoids mixing "what I am reading now" with "what I have already kept".
#
# Invariant:
# - `nums[:write]` is always a valid prefix where each value appears at most twice.
# - When `write < 2`, the current value is always safe to keep.
# - When `write >= 2`, compare `nums[read]` with `nums[write - 2]`.
#   If they are different, writing the current value will not create three copies.


# Better Version
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(len(nums)):
            if write < 2 or nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
