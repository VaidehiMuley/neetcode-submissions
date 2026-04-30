# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def recursion(l1_node, l2_node, carry):
            if not l1_node and not l2_node and not carry:
                return None
            sum_val = ((l1_node.val if l1_node else 0)+
                      (l2_node.val if l2_node else 0) + 
                      carry)
            result_val = sum_val %10
            carry = sum_val //10
            result = ListNode(result_val)
            result.next = recursion(l1_node.next if l1_node else None, l2_node.next if l2_node else None, carry)
            return result

        return recursion(l1, l2, 0)
            

        