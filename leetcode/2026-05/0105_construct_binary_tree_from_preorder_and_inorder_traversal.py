# Pattern: Recursive DFS with index map
# Time: O(n)
# Space: O(n)
# Mistakes: The first version had the right recursion, but relied on
# LeetCode-provided annotation names and only kept the key idea as inline notes.

from __future__ import annotations

from typing import List, Optional


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
    #     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #         # root -> left -> right:
    #         # root => preorder;
    #         # left size => inorder_root_index - inorder_left;
    #         inorder_index = {val: i for i, val in enumerate(inorder)}
    #
    #         def _build(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
    #             if pre_left > pre_right:
    #                 return None
    #             root_val = preorder[pre_left]
    #             root = TreeNode(root_val)
    #
    #             root_index = inorder_index[root_val]
    #             left_size = root_index - in_left
    #
    #             root.left = _build(pre_left+1, pre_left+left_size, in_left, root_index-1)
    #             root.right = _build(pre_left+left_size+1, pre_right, root_index+1, in_right)
    #             return root
    #
    #         return _build(0, len(preorder)-1, 0, len(inorder)-1)
    #
    # Key Point:
    # Preorder gives the current root first. Use that root's inorder index to
    # split left and right subtrees; the left subtree size then determines both
    # preorder child ranges.
    #
    # Better Version:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        def build(
            pre_left: int,
            pre_right: int,
            in_left: int,
            in_right: int,
        ) -> Optional[TreeNode]:
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            root_index = inorder_index[root_val]
            left_size = root_index - in_left

            root.left = build(
                pre_left + 1,
                pre_left + left_size,
                in_left,
                root_index - 1,
            )
            root.right = build(
                pre_left + left_size + 1,
                pre_right,
                root_index + 1,
                in_right,
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
