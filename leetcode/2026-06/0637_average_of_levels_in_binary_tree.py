# Pattern: Level-order BFS
# Time: O(n)
# Space: O(w)
# Mistakes: The first version had the right level-order idea, but relied on
# LeetCode-provided annotation names and used an unnecessary nested helper.

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
    #     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    #         res = []
    #         def bfs(root):
    #             level = deque([root])
    #
    #             while level:
    #                 size = len(level)
    #                 s = 0
    #                 for i in range(size):
    #                     node = level.popleft()
    #                     s = s + node.val
    #                     if node.left:
    #                         level.append(node.left)
    #                     if node.right:
    #                         level.append(node.right)
    #                 res.append(float(s)/float(size))
    #
    #         bfs(root)
    #         return res
    #
    # Key Point:
    # Freeze the queue length at the start of each level. Sum exactly those
    # nodes, enqueue their children, then divide by that level size.
    #
    # Better Version:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        averages = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / level_size)

        return averages
