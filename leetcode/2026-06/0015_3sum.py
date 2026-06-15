# Pattern: Sort plus two pointers
# Time: O(n^2)
# Space: O(1) extra, not counting the output
# Mistakes: The first version appended partial triples before finding a match,
# did not move pointers after a match, and did not skip duplicates.


class Solution:
    # Original Code:
    # class Solution:
    #     def threeSum(self, nums: list[int]) -> list[list[int]]:
    #         nums.sort()
    #         res = []
    #         for i, v in enumerate(nums):
    #             target = 0 - v
    #             res.append([v])
    #             left = i+1
    #             right = len(nums) - 1
    #             while left < right:
    #                 if nums[left] + nums[right] < target:
    #                     left = left + 1
    #                 elif nums[left] + nums[right] > target:
    #                     right = right - 1
    #                 else:
    #                     res[-1].append(nums[left])
    #                     res[-1].append(nums[right])
    #         return res
    #
    # Key Point:
    # Sort first. Fix one number, then use two pointers to find pairs summing
    # to its opposite. Skip duplicate fixed values and duplicate pairs.
    #
    # Better Version:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, value in enumerate(nums):
            if value > 0:
                break
            if i > 0 and value == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
