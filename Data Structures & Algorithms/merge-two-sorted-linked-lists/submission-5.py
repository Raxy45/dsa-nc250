# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = root = None
        if not list1 or not list2:
            return list2 if list2 else list1 
            
        while list1 and list2:
            if list1.val<list2.val:
                if not root:
                    root = list1
                    curr = list1
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if not root:
                    root = list2
                    curr = root
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
        
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        return root
