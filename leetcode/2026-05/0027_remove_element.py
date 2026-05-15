from typing import List


# Original Code
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         read = 0
#         write = 0
#         while read < len(nums):
#             if nums[read] != val:
#                 nums[write] = nums[read]
#                 write = write + 1
#             read = read + 1
#         return write
#
# Key Point
# Use two pointers to compact the array in place:
# - `read` scans every original element.
# - `write` marks the next slot in the kept prefix.
# Only copy values that are not equal to `val`.
# The final answer is the length of the kept prefix, `write`.


# Better Version
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
