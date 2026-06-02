# Pattern: Recursive divide and conquer
# Time: O(n)
# Space: O(log n)
# Mistakes: The first version inserted values into a BST after splitting, which
# can still create a skewed tree and loops forever for an empty list.

from __future__ import annotations

from typing import List, Optional


class Solution:
    # Original Code:
    # class Solution:
    #     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #         def insert(root, val):
    #             if root is None:
    #                 return TreeNode(val)
    #             if val < root.val:
    #                 root.left = insert(root.left, val)
    #             else:
    #                 root.right = insert(root.right, val)
    #             return root
    #
    #         r = None
    #
    #         def dc(nums, r):
    #             if len(nums) == 1:
    #                 r = insert(r, nums[0])
    #                 return r
    #             else:
    #                 r = dc(nums[:len(nums)//2], r)
    #                 r = dc(nums[len(nums)//2:], r)
    #             return r
    #         r = dc(nums, r)
    #
    #         return r
    #
    # Key Point:
    # Choose the middle value as the root so left and right subarrays have
    # similar sizes; recursively build child subtrees from those ranges.
    #
    # Better Version:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)
