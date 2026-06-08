from typing import List


# Pattern: Binary search
# Time: O(log n)
# Space: O(log n)
# Mistakes: The first version used a closed range and recursed with
# `binary(mid, e)`, which can repeat the same range forever.


class Solution:
    # Original Code:
    # class Solution:
    #     def searchInsert(self, nums: List[int], target: int) -> int:
    #         def binary(s, e, target: int) -> int:
    #             if s >= e:
    #                 return s
    #
    #             mid = (s + e) // 2
    #             if nums[mid] == target:
    #                 return mid
    #             if nums[mid] > target:
    #                 return binary(s, mid, target)
    #             else:
    #                 return binary(mid, e, target)
    #
    #         return binary(0, len(nums)-1, target)
    #
    # Key Point:
    # Use a half-open search range `[left, right)`, so `right = len(nums)`.
    # This lets the answer be any insertion index from `0` through `len(nums)`.
    # When `nums[mid] < target`, move to `mid + 1` so the range always shrinks.
    #
    # Better Version:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(left: int, right: int) -> int:
            if left >= right:
                return left

            mid = (left + right) // 2
            if nums[mid] >= target:
                return binary(left, mid)
            return binary(mid + 1, right)

        return binary(0, len(nums))
