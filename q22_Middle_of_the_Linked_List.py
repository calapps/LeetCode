# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slowptr = head
        fastptr = head

        while fastptr != None and fastptr.next != None:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        
        return slowptr