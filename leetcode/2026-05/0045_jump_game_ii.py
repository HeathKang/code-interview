# Pattern: Greedy / layer expansion
# Time: O(n)
# Space: O(1)
# Mistakes: The first version used slicing in the loop, which created extra memory
# and made the invariant harder to read.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def jump(self, nums: List[int]) -> int:
    #         steps = 0
    #         current_bound = 0
    #         far = 0
    #         for i, step in enumerate(nums[:-1]):
    #             far = max(far, i + step)
    #             if i == current_bound:
    #                 steps = steps + 1
    #                 current_bound = far
    #         return steps
    #
    # Key Point:
    # Each jump expands the current reachable layer. When the scan reaches the
    # end of the current layer, commit one jump and extend to the farthest index
    # reachable from that layer.
    #
    # Better Version:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
