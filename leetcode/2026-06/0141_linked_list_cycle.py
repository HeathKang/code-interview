# Pattern: Slow/fast pointers
# Time: O(n)
# Space: O(1)

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Original Code:
    # No original attempt was provided.
    #
    # Key Point:
    # Move slow one step and fast two steps. If a cycle exists, fast eventually
    # catches slow; otherwise, fast reaches the end of the list.
    #
    # Better Version:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
