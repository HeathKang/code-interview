# Pattern: Linked-list merge sort
# Time: O(n log n)
# Space: O(log n)
# Mistakes: The first slow/fast version split the list correctly, but missed
# the recursive base case inside sort().

from __future__ import annotations

from typing import Optional


class Solution:
    # Original Code:
    # class Solution:
    #     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #         dummy = ListNode(0)
    #
    #         if head is None or head.next is None:
    #             return head
    #
    #         def sort(head: Optional[ListNode]) -> Optional[ListNode]:
    #             slow = head
    #             fast = head.next
    #
    #             while fast and fast.next:
    #                 slow = slow.next
    #                 fast = fast.next.next
    #
    #             right = slow.next
    #             slow.next = None
    #
    #             left = sort(head)
    #             right = sort(right)
    #             return _merge(left, right)
    #
    #         def _merge(left: Optional[ListNode], right:Optional[ListNode]) -> Optional[ListNode]:
    #             dummy = ListNode()
    #             tail = dummy
    #
    #             while left and right:
    #                 if left.val <= right.val:
    #                     tail.next = left
    #                     left = left.next
    #                 else:
    #                     tail.next = right
    #                     right = right.next
    #                 tail = tail.next
    #
    #             tail.next = left if left else right
    #             return dummy.next
    #
    #         return sort(head)
    #
    # Key Point:
    # Use slow/fast pointers to find the middle: slow moves one step and fast
    # moves two. Starting fast at head.next makes slow stop at the left tail,
    # so slow.next can become the right half before cutting the list.
    #
    # Better Version:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None:
                return head

            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            right = slow.next
            slow.next = None

            left = sort(head)
            right = sort(right)
            return merge(left, right)

        def merge(
            left: Optional[ListNode],
            right: Optional[ListNode],
        ) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy

            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left if left else right
            return dummy.next

        return sort(head)
