# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        carry = 0
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            if curr_sum > 9:
                carry = curr_sum//10
            curr_sum = curr_sum%10
            curr.next = ListNode(curr_sum)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        
        if carry>0:
            curr.next = ListNode(carry)
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return dummy.next