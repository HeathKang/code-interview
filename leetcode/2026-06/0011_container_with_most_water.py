from typing import List


# Pattern: Two pointers with upper-bound pruning
# Time: O(n)
# Space: O(1)
# Mistakes: The first version used the right movement rule, but the file was
# missing the `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def maxArea(self, height: List[int]) -> int:
    #         left = 0
    #         right = len(height) - 1
    #         contain = 0
    #         while left < right:
    #             m = (right-left)*min(height[right], height[left])
    #             contain = max(contain, m)
    #             if height[left] < height[right]:
    #                 left = left + 1
    #             else:
    #                 right = right -1
    #
    #         return contain
    #
    # Key Point:
    # Move the shorter side because it is the limiting height. With that same
    # short side fixed, every future width is smaller, so none of those pairs
    # can beat the pair already checked. This safely discards that boundary.
    #
    # Better Version:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            width = right - left
            water_height = min(height[left], height[right])
            best = max(best, width * water_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
