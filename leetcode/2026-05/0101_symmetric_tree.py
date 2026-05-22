# Pattern: Recursive DFS
# Time: O(n)
# Space: O(h)
# Mistakes: The first version had the right mirror recursion, but relied on
# LeetCode-provided annotation names and did not handle root being None.

from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Original Code:
    # # Definition for a binary tree node.
    # # class TreeNode:
    # #     def __init__(self, val=0, left=None, right=None):
    # #         self.val = val
    # #         self.left = left
    # #         self.right = right
    # class Solution:
    #     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #         def isSym(left, right) -> bool:
    #             if not left and not right:
    #                 return True
    #             if left and right:
    #                 if left.val == right.val:
    #                     return isSym(left.left, right.right) and isSym(left.right,right.left)
    #                 else:
    #                     return False
    #             return False
    #
    #         return isSym(root.left, root.right)
    #
    # Key Point:
    # A tree is symmetric when its left and right subtrees are mirrors: outer
    # children match each other, and inner children match each other.
    #
    # Better Version:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left is right

            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        if root is None:
            return True

        return isMirror(root.left, root.right)
