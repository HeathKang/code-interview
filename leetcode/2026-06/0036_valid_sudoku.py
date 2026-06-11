from typing import List


# Pattern: Hash set
# Time: O(1)
# Space: O(1)
# Mistakes: The first version used the right uniqueness encoding, but the file
# was missing the `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def isValidSudoku(self, board: List[List[str]]) -> bool:
    #         seen = set()
    #
    #         for row in range(9):
    #             for col in range(9):
    #                 if board[row][col] == ".":
    #                     continue
    #                 value = board[row][col]
    #                 box = (row//3, col//3)
    #                 keys = (
    #                     ("row", row, value),
    #                     ("col", col, value),
    #                     ("box", box, value)
    #                 )
    #                 for k in keys:
    #                     if k in seen:
    #                         return False
    #                     else:
    #                         seen.add(k)
    #
    #         return True
    #
    # Key Point:
    # A filled cell must be unique in its row, column, and 3x3 box. Encode each
    # constraint as a key in a set; if the same key appears again, the board is
    # invalid. Empty cells do not matter because the board does not need to be
    # solvable.
    #
    # Better Version:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue

                box = (row // 3, col // 3)
                keys = (
                    ("row", row, value),
                    ("col", col, value),
                    ("box", box, value),
                )

                for key in keys:
                    if key in seen:
                        return False
                    seen.add(key)

        return True
