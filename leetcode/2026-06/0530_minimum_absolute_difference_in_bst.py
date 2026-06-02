# Pattern: BST inorder traversal
# Time: O(n)
# Space: O(h)
# Mistakes: The first version built the full sorted list; only the previous
# inorder value is needed.

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
    #     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #         order = []
    #         def inorder(root):
    #             if root is None:
    #                 return []
    #             return inorder(root.left)+[root.val]+inorder(root.right)
    #
    #         order = inorder(root)
    #         m = order[1]-order[0]
    #         for i in range(1, len(order)-1):
    #             if order[i+1] - order[i] < m:
    #                 m = order[i+1] - order[i]
    #
    #         return m
    #
    # Key Point:
    # Inorder traversal of a BST visits values in sorted order, so the minimum
    # absolute difference must be between two adjacent inorder values.
    #
    # Better Version:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        best = float("inf")

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, best
            if node is None:
                return

            inorder(node.left)

            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val

            inorder(node.right)

        inorder(root)
        return best
