# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.get_kth(groupPrev, k)
            groupNext = kth.next

            curr = groupNext.next
            prev = kth.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            ## The node which was group's first node initially will be last now
            tmp = groupPrev.next
            ## Link groupPrev to kth such that now it becomes first element of the current group
            groupPrev.next = kth
            ## Update groupPrev to the last element of the prev group (which was initially the first element of that group)
            groupPrev = tmp 
        return dummy.next
            
            

    def get_kth(self, node,k):
        ## Get the kth node
        while node and k > 0:
            node = node.next
            k -=1
        return node