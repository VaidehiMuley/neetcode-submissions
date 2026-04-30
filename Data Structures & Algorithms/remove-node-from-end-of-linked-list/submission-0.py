# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        ## Shift right by n
        while n>0 and right:
            right = right.next
            n -=1
        
        ## Shift right and left pointer
        while right:
            left = left.next
            right = right.next
        
        ## Remove the nth node from the end
        left.next = left.next.next
        return dummy.next
        