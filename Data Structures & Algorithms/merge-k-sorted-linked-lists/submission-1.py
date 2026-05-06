# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                result = self.mergelists(l1,l2)
                mergedlists.append(result)
            lists = mergedlists
        return lists[0]
        
    def mergelists(self, list1, list2):
        dummy = ListNode()
        result = dummy

        ## While both are present
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next

            else:
                result.next = list2
                list2 = list2.next
                
        # When we are only left with one LL
        result.next = list1 or list2
        