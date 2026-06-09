from typing import List


# Pattern: Two pointers
# Time: O(n)
# Space: O(1)
# Mistakes: The first version used the right algorithm, but the file was
# missing the `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #         left = 0
    #         right = len(numbers) - 1
    #         while left < right:
    #             if numbers[left] + numbers[right] == target:
    #                 return [left+1, right+1]
    #             if numbers[left] + numbers[right] > target:
    #                 right = right - 1
    #             else:
    #                 left = left + 1
    #         return []
    #
    # Key Point:
    # Because `numbers` is sorted, a sum that is too small must move `left`
    # rightward, and a sum that is too large must move `right` leftward.
    #
    # Better Version:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1

        return []
