# Pattern: Recursive DFS
# Time: O(n)
# Space: O(h)
# Mistakes: The first version was correct, but relied on LeetCode-provided
# annotation names and used an unnecessary nested helper.

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
    #     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #         def invert(t: Optional[TreeNode]):
    #             if t:
    #                 t.left, t.right = t.right, t.left
    #                 invert(t.left)
    #                 invert(t.right)
    #
    #         invert(root)
    #         return root
    #
    # Key Point:
    # Swap the current node's children, then recursively invert both subtrees.
    # Returning the same root preserves the tree identity with inverted links.
    #
    # Better Version:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
