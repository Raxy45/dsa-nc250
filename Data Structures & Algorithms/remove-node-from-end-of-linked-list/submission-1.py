# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_length = 0
        temp = head
        while temp:
            temp = temp.next
            ll_length += 1
        
        if ll_length<=1:
            return None
        required_node = ll_length-n
        temp = head
        i = 0
        print(i, required_node, ll_length)
        while i<required_node-1:
            temp = temp.next
            i += 1
        print(temp.val)
        if temp.next:
            temp.next = temp.next.next
        else:
            temp.next=None
        return head