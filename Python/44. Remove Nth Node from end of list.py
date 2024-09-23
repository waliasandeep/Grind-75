# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #1 Create a dummy record before head
        dummy = ListNode(0, head)
        #2. Make left = dummy and right = head
        left, right = dummy, head
        #Keep incrementing right until the distance between left and right is n
        while n > 0:
            right = right.next
            n -= 1
        #3. Increment both left and right until right reaches the end
        #This will make left reach just before the pointer to be removed
        while right:
            left = left.next
            right = right.next
        
        #Remove the node by updating left next pointer
        left.next = left.next.next

        return dummy.next