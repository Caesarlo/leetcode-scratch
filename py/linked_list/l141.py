from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        dummy_head = ListNode()
        dummy_head.next = head

        slow = dummy_head.next
        fast = dummy_head.next.next

        while fast != None and fast.next != None:

            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next

        return False
