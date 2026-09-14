# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#  head ->  1,20 -> 2,30 -> 3,40 -> 4,null -> Null
#   10       10.  20.  30.  40
#  Null <- 1,null <- 2,10 <- 3,20 <- 4,30 <- head,40
#           
 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev





        