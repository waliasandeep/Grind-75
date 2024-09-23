# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        #1. Iterate till the end using fast and slow pointer
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast= fast.next.next
        """
        1->2->3->4->5
              S     F
        """
        
        #2. Reverse the second half
        prev,curr = None, slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3.Cut off the first half
        slow.next = None
        
        # 4. Merge two halves
        first, second = head, prev
        while first and second:
            tempFirstNext = first.next
            first.next = second
            tempSecondNext = second.next
            second.next = tempFirstNext
            first = tempFirstNext
            second = tempSecondNext