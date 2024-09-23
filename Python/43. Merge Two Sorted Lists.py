# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = mergeList = ListNode(0)
        while list1 or list2:
            if list1 == None:
                mergeList.next = list2
                break
            elif list2 == None:
                mergeList.next = list1
                break
            else:
                if list1.val <= list2.val:
                    mergeList.next = list1
                    list1 = list1.next
                else:
                    mergeList.next = list2
                    list2 = list2.next
            mergeList = mergeList.next
        
        return head.next