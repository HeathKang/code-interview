# Pattern: Prefix and suffix accumulation
# Time: O(n)
# Space: O(1)
# Mistakes: The first version left the invariant implicit and skipped the import.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def productExceptSelf(self, nums: List[int]) -> List[int]:
    #         # nums i is prefix * suffix
    #         # one loop for prefix
    #         # one loop for suffix
    #         res = [ 1 for _ in nums ]
    #         prefix = 1
    #         suffix = 1
    #         for i in range(len(nums)):
    #             res[i] = prefix
    #             prefix = prefix * nums[i]
    #
    #         for i in range(len(nums)-1, -1, -1):
    #             res[i] = suffix * res[i]
    #             suffix = suffix * nums[i]
    #
    #         return res
    #
    # Key Point:
    # The forward pass stores the product of everything to the left of each
    # index. The backward pass multiplies in the product of everything to the
    # right.
    #
    # Better Version:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
