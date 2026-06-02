# Pattern: Recursive DFS with bounds
# Time: O(n)
# Space: O(h)
# Mistakes: The first version had the right invariant; keep the bounds helper
# explicit and use consistent naming/format.

from __future__ import annotations

from typing import Optional


class Solution:
    # Original Code:
    # # Definition for a binary tree node.
    # # class TreeNode:
    # #     def __init__(self, val=0, left=None, right=None):
    # #         self.val = val
    # #         self.left = left
    # #         self.right = right
    # class Solution:
    #     def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #         def validBST(root, low=float("-inf"), high=float("inf")):
    #             if not root:
    #                 return True
    #             if not (low < root.val < high):
    #                 return False
    #             return validBST(root.left,low,root.val) and validBST(root.right, root.val, high)
    #
    #         return validBST(root)
    #
    # Key Point:
    # Each node must fit the valid range inherited from all ancestors, not just
    # compare against its direct parent.
    #
    # Better Version:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True

            if not low < node.val < high:
                return False

            return (
                is_valid(node.left, low, node.val)
                and is_valid(node.right, node.val, high)
            )

        return is_valid(root, float("-inf"), float("inf"))
