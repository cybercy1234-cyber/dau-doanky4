# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Step 1: Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Step 2: Move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # Step 3: Remove target node
        second.next = second.next.next

        return dummy.next
            