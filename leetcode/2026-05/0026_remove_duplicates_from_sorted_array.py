from typing import List


# Original Code
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left = 0
#         right = 0
#         while right < len(nums):
#             if nums[left] == nums[right]:
#                 right = right + 1
#             else:
#                 nums[left + 1] = nums[right]
#                 left = left + 1
#         return left + 1
#
# Key Point
# Use two pointers on the sorted array:
# - `write` marks the end of the unique prefix.
# - `read` scans forward looking for the next new value.
# When `nums[read] != nums[write]`, copy that new value to `write + 1`.
# The main fix versus the original version is handling `[]` explicitly.


# Better Version
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 0
        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1
