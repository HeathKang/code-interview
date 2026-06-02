# Pattern: BST inorder traversal
# Time: O(h + k)
# Space: O(h)
# Mistakes: The first version built every sorted value; stop as soon as the
# kth inorder node is visited.

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
    #     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #         def inorder(root):
    #             if not root:
    #                 return []
    #             return inorder(root.left)+[root.val]+inorder(root.right)
    #
    #         order = inorder(root)
    #         return order[k-1]
    #
    # Key Point:
    # Inorder traversal of a BST visits values in ascending order, so the kth
    # smallest value is the kth node visited by inorder traversal.
    #
    # Better Version:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right

        raise ValueError("k is larger than the number of nodes")
