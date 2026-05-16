# Original Code
# No original attempt recorded.
#
# Key Point
# The problem is not asking us to print the zigzag shape. It asks for the
# string obtained by reading the zigzag row by row.
#
# Example: s = "PAYPALISHIRING", numRows = 4
#
# Row 0: P     I     N
# Row 1: A   L S   I G
# Row 2: Y A   H R
# Row 3: P     I
#
# Read rows from top to bottom:
# "P" + "I" + "N" + "A" + "L" + "S" + "I" + "G" + ...
# Result: "PINALSIGYAHRPI"
#
# The easiest implementation is row simulation:
# - Keep one buffer for each row.
# - Keep the current row index.
# - Move down with step = 1.
# - When the current row reaches the bottom, change step to -1.
# - When the current row reaches the top, change step back to 1.
#
# For numRows = 4, row movement repeats like this:
#
# char: P A Y P A L I S H I R I N G
# row:  0 1 2 3 2 1 0 1 2 3 2 1 0 1
# step: v v v ^ ^ ^ v v v ^ ^ ^ v v
#
# That row sequence is enough. We do not need a 2D matrix with spaces because
# only the row order matters in the final answer.
#
# Edge cases:
# - If `numRows == 1`, there is no zigzag.
# - If `numRows >= len(s)`, each character stays in order.
#
# Common mistake:
# - Forgetting `numRows == 1`. Without that guard, the row index can move out
#   of range because there is no second row to move to.
#
# Time: O(n), where n is len(s).
# Space: O(n), for the row buffers and final answer.


# Better Version
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        row = 0
        step = 1

        for char in s:
            rows[row].append(char)

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return "".join("".join(row_chars) for row_chars in rows)
