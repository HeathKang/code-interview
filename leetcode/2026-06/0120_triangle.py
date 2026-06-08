from typing import List


# Pattern: Top-down DP
# Time: O(n^2)
# Space: O(n^2)
# Mistakes: The latest version fixed the edge-parent logic. The remaining
# cleanup is to memoize only solved states instead of pre-filling with `inf`.


class Solution:
    # Original Code:
    # class Solution:
    #     def minimumTotal(self, triangle: List[List[int]]) -> int:
    #         mem = {}
    #         for i in range(len(triangle)):
    #             for j in range(len(triangle[i])):
    #                 mem[(i,j)] = float("inf")
    #
    #         def dp(i,j:int) -> int:
    #             if (i,j) in mem:
    #                 if mem[(i,j)] != float("inf"):
    #                     return mem[(i,j)]
    #
    #             if (i,j) == (0,0):
    #                 mem[(0,0)] = triangle[0][0]
    #                 return mem[(0,0)]
    #
    #             if j == 0:
    #                 ans = dp(i-1,j)+triangle[i][j]
    #             elif j == i:
    #                 ans = dp(i-1,j-1)+triangle[i][j]
    #             else:
    #                 ans = min(dp(i-1,j-1), dp(i-1, j))+triangle[i][j]
    #             mem[(i,j)] = ans
    #             return ans
    #
    #         small = float("inf")
    #         for j in range(len(triangle[-1])):
    #             small = min(small, dp(len(triangle)-1, j))
    #         return small
    #
    # Key Point:
    # State: `dp(i, j)` is the minimum path sum from the top to cell `(i, j)`.
    # Transition: left edge has one parent `(i - 1, j)`, right edge has one
    # parent `(i - 1, j - 1)`, and middle cells take the smaller of both.
    # Answer: take the minimum `dp` value across the last row.
    #
    # Better Version:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                return triangle[0][0]

            if j == 0:
                best = dp(i - 1, j)
            elif j == i:
                best = dp(i - 1, j - 1)
            else:
                best = min(dp(i - 1, j - 1), dp(i - 1, j))

            memo[(i, j)] = best + triangle[i][j]
            return memo[(i, j)]

        last_row = len(triangle) - 1
        return min(dp(last_row, j) for j in range(len(triangle[last_row])))
