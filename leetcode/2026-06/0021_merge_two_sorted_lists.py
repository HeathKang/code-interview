# Pattern: Two pointers
# Time: O(m + n)
# Space: O(1)
# Mistakes: The original version was correct, but used extra branching and an
# unclear tail-pointer name.

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Original Code:
    # def mergeTwoLists(self, list1, list2):
    #     dummy = ListNode()
    #     dummy3 = dummy
    #     while list1 or list2:
    #         if list1 and list2:
    #             if list1.val > list2.val:
    #                 dummy3.next = list2
    #                 list2 = list2.next
    #             else:
    #                 dummy3.next = list1
    #                 list1 = list1.next
    #         elif list1:
    #             dummy3.next = list1
    #             break
    #         else:
    #             dummy3.next = list2
    #             break
    #         dummy3 = dummy3.next
    #     return dummy.next
    #
    # Key Point:
    # While both lists remain, link the smaller current node and advance only
    # that list. Then attach the entire remaining sorted suffix in one step.
    #
    # Better Version:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next
