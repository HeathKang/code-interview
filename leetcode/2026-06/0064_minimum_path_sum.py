from typing import List


# Pattern: Top-down DP
# Time: O(m * n)
# Space: O(m * n)
# Mistakes: The recurrence was correct. The main cleanup is adding the standard
# review template and keeping memoization focused on solved states.


class Solution:
    # Original Code:
    # class Solution:
    #     def minPathSum(self, grid: List[List[int]]) -> int:
    #         mem = {}
    #
    #         def dp(i,j: int) -> int:
    #             if (i,j) in mem:
    #                 return mem[(i,j)]
    #             if i == 0:
    #                 if j == 0:
    #                     mem[(i,j)] = grid[0][0]
    #                 else:
    #                     mem[(i,j)] = grid[0][j] + dp(0,j-1)
    #                 return mem[(i,j)]
    #
    #             if j == 0:
    #                 ans = dp(i-1,j)+grid[i][j]
    #             else:
    #                 ans = min(dp(i-1,j),dp(i,j-1)) + grid[i][j]
    #
    #             mem[(i,j)] = ans
    #             return ans
    #
    #         return dp(len(grid)-1, len(grid[-1])-1)
    #
    # Key Point:
    # State: `dp(i, j)` is the minimum path sum from `(0, 0)` to `(i, j)`.
    # Transition: first row can only come from left, first column can only come
    # from above, and every other cell takes the smaller of those two parents.
    # Answer: return `dp(last_row, last_col)`.
    #
    # Better Version:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}

        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                return grid[0][0]

            if i == 0:
                best = dp(i, j - 1)
            elif j == 0:
                best = dp(i - 1, j)
            else:
                best = min(dp(i - 1, j), dp(i, j - 1))

            memo[(i, j)] = best + grid[i][j]
            return memo[(i, j)]

        return dp(len(grid) - 1, len(grid[0]) - 1)
