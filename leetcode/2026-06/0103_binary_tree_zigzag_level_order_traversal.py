# Pattern: Level-order BFS
# Time: O(n)
# Space: O(w)
# Mistakes: The first version was correct, but relied on LeetCode-provided
# annotation names and used an unnecessary nested helper.

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
    # from collections import deque
    #
    # class Solution:
    #     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #         if not root:
    #             return []
    #         res = []
    #         def bfs(root):
    #             level = deque([root])
    #             order = True
    #
    #             while level:
    #                 size = len(level)
    #                 current = []
    #
    #                 for i in range(size):
    #                     node = level.popleft()
    #                     current.append(node.val)
    #                     if node.left:
    #                         level.append(node.left)
    #                     if node.right:
    #                         level.append(node.right)
    #
    #                 if not order:
    #                     current.reverse()
    #                 order = not order
    #                 res.append(current)
    #
    #         bfs(root)
    #         return res
    #
    # Key Point:
    # Process normal BFS levels, then flip the output order for every other
    # level. Children are still enqueued left-to-right for stable traversal.
    #
    # Better Version:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                current_level.reverse()

            levels.append(current_level)
            left_to_right = not left_to_right

        return levels

