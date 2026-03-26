from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        dummy_head = ListNode()
        dummy_head.next = head

        fast = dummy_head
        slow = dummy_head

        while n:
            fast = fast.next
            n -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next

        slow.next = slow.next.next

        del temp

        return dummy_head.next
