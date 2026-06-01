# Pattern: Right-first DFS / Level-order BFS
# Time: O(n)
# Space: O(h) for DFS, O(w) for BFS
# Mistakes: The first version was correct, but relied on LeetCode-provided
# annotation names and kept rough drafting notes in the executable method.

from __future__ import annotations

from collections import deque
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
    #     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #         # DFS
    #         # 1. def dfs(root, state)
    #         #        solve
    #         #        dfs(root.right/left, state)
    #         res = []
    #
    #         def dfs(root, depth):
    #             if root:
    #                 if depth == len(res):
    #                     res.append(root.val)
    #                 dfs(root.right, depth + 1)
    #                 dfs(root.left, depth + 1)
    #
    #         dfs(root, 0)
    #         return res
    #
    # Key Point:
    # Visit right child before left child. The first node reached at each depth
    # is the node visible from the right side.
    #
    # Better Version:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return

            if depth == len(view):
                view.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return view

    # BFS Version:
    def rightSideViewBfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        view = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    view.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return view
