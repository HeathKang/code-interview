from typing import List


# Pattern: Sort then merge
# Time: O(n log n)
# Space: O(n), for the output
# Mistakes: The first version used the right merge condition, but the file was
# missing the `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #         intervals.sort()
    #         res = [intervals[0]]
    #         for i in range(1, len(intervals)):
    #             if res[-1][-1] >= intervals[i][0]:
    #                 res[-1][-1] = max(res[-1][-1], intervals[i][-1])
    #             else:
    #                 res.append(intervals[i])
    #         return res
    #
    # Key Point:
    # Sort intervals by start. The last merged interval is the only possible
    # overlap candidate for the next interval; merge when its end reaches the
    # next start, otherwise append a new interval.
    #
    # Better Version:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
