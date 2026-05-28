# Pattern: Recursive DFS with index map
# Time: O(n)
# Space: O(n)
# Mistakes: The first version had the right recursion, but relied on
# LeetCode-provided annotation names and only kept the key idea in the code.

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
    #     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #         inorder_index = {val: i for i, val in enumerate(inorder)}
    #
    #         def build(post_l, post_r, in_l, in_r) -> Optional[TreeNode]:
    #             if post_l > post_r:
    #                 return None
    #
    #             root_val = postorder[post_r]
    #             root = TreeNode(root_val)
    #
    #             root_index = inorder_index[root_val]
    #             right_size = in_r - root_index
    #
    #             root.right = build(post_r-right_size, post_r-1, root_index+1,in_r)
    #             root.left = build(post_l,post_r-right_size-1, in_l, root_index-1)
    #
    #             return root
    #
    #         return build(0, len(postorder)-1, 0, len(inorder)-1)
    #
    # Key Point:
    # Postorder gives the current root last. Use that root's inorder index to
    # split left and right subtrees; the right subtree size determines the
    # postorder range immediately before the root, and the remaining prefix is
    # the left subtree.
    #
    # Better Version:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        def build(
            post_left: int,
            post_right: int,
            in_left: int,
            in_right: int,
        ) -> Optional[TreeNode]:
            if post_left > post_right:
                return None

            root_val = postorder[post_right]
            root = TreeNode(root_val)

            root_index = inorder_index[root_val]
            right_size = in_right - root_index

            root.left = build(
                post_left,
                post_right - right_size - 1,
                in_left,
                root_index - 1,
            )
            root.right = build(
                post_right - right_size,
                post_right - 1,
                root_index + 1,
                in_right,
            )

            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
