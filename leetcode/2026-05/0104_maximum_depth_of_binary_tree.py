# Pattern: Recursive DFS
# Time: O(n)
# Space: O(h)
# Mistakes: The first version had the right recursion idea, but relied on
# LeetCode-provided annotation names and carried depth as extra state.

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
    #     def maxDepth(self, root: Optional[TreeNode]) -> int:
    #         def travel(tree: Optional[TreeNode], dep) -> int:
    #             if tree:
    #                 dep = dep + 1
    #                 dep = max(travel(tree.left, dep), travel(tree.right, dep))
    #             return dep
    #         d = travel(root, 0)
    #         return d
    #
    # Key Point:
    # The depth of an empty tree is 0. Otherwise, it is 1 plus the deeper child
    # subtree.
    #
    # Better Version:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
