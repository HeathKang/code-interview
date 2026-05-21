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
    #     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #         def travel(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #             if p and q:
    #                 if p.val != q.val:
    #                     return False
    #                 else:
    #                     return travel(p.left, q.left) and travel(p.right, q.right)
    #             if not p and not q:
    #                 return True
    #             else:
    #                 return False
    #         return travel(p,q)
    #
    # Key Point:
    # Two trees are the same only when the current nodes match and both child
    # subtree pairs are also the same.
    #
    # Better Version:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
