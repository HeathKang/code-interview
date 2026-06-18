from typing import List


# Pattern: One-pass range scan
# Time: O(n)
# Space: O(1), excluding the output
# Mistakes: The first version used a hash set like Longest Consecutive
# Sequence, but this input is already sorted and unique, so adjacent indexes
# are enough. The file also needed the `List` import.


class Solution:
    # Original Code:
    # class Solution:
    #     def summaryRanges(self, nums: List[int]) -> List[str]:
    #         values = set(nums)
    #         res = []
    #
    #         for num in nums:
    #             if num - 1 in values:
    #                 continue
    #             current = num
    #             res.append([current])
    #             while current + 1 in values:
    #                 current = current + 1
    #
    #             if current not in res[-1]:
    #                 res[-1].append(current)
    #
    #         res = [
    #             f"{r[0]}->{r[1]}" if len(r) == 2 else f"{r[0]}"
    #             for r in res
    #         ]
    #
    #         return res
    #
    # Key Point:
    # Because `nums` is sorted and has no duplicates, a range continues exactly
    # while the next value is `previous + 1`. Track the start, advance to the
    # end of the current run, then format one output string.
    #
    # Better Version:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        index = 0

        while index < len(nums):
            start = nums[index]

            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1

            end = nums[index]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")

            index += 1

        return ranges
