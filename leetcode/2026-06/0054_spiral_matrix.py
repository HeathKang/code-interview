from typing import List


# Pattern: Matrix boundary simulation
# Time: O(m * n)
# Space: O(1) extra, excluding the output list
# Mistakes: The first version simulated direction changes directly, but it
# started by moving right even for a single-column matrix and was missing the
# `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #         direct = ["r","d","l","u"]
    #         res = list()
    #         rowl = len(matrix)-1
    #         coll = len(matrix[0])-1
    #         row = 0
    #         col = 0
    #         i = 0
    #         cycle = 0
    #         m = len(matrix) * len(matrix[0])
    #
    #         def _ne(i):
    #             if i == 3:
    #                 i = 0
    #             else:
    #                 i = i +  1
    #             return i
    #
    #         while len(res) < m:
    #             res.append(matrix[row][col])
    #             dire = direct[i]
    #             if dire == "r":
    #                 col = col + 1
    #                 if col == coll-cycle:
    #                     i = _ne(i)
    #             elif dire == "d":
    #                 row = row + 1
    #                 if row == rowl-cycle:
    #                     i = _ne(i)
    #             elif dire == "l":
    #                 col = col - 1
    #                 if col == cycle:
    #                     i = _ne(i)
    #             elif dire == "u":
    #                 row = row - 1
    #                 if row == cycle+1:
    #                     i = _ne(i)
    #                     cycle = cycle + 1
    #
    #         return res
    #
    # Key Point:
    # Keep four boundaries: top, bottom, left, and right. Traverse one edge,
    # then move that boundary inward. Before traversing bottom or left, check
    # that the remaining rectangle still has rows and columns.
    #
    # Better Version:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
