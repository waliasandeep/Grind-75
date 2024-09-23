class Node(object):
    def __init__(self, val : int= 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head : Node) -> Node:
        curr = head
        prev = None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev 
