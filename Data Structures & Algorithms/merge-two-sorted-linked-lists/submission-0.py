# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans_head = None
        ans_node = None
        c1, c2 = list1, list2
        c = 0
        while (c1 and c2) and c<20:
            print(c1.val, c2.val)
            c += 1
            if c1.val<c2.val:
                if ans_head is None:
                    ans_head = ans_node = c1
                else:
                    ans_node.next=c1
                c1 = c1.next
            else:
                if ans_head is None:
                    ans_head = ans_node = c2
                else:
                    ans_node.next=c2
                c2 = c2.next
            ans_node = ans_node.next
            c += 1
        
        if c1:
            ans_node.next=c1
        
        if c2:
            ans_node.next = c2
        
        return ans_head