# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1 
                list1, head = list1.next, list1 
            else:
                head.next = list2 
                list2, head = list2.next, list2 
        
        if list1 or list2:
            head.next = list1 or list2 

        return dummy.next 
        

# list1 = [1,2,3]
# list2 = [2,5,6]
# head = [[1,1], [2,2], [1,2], [1,3], [2,5], [2,6]]