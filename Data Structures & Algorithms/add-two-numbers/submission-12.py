# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        carry = 0
        while l1 or l2:
            curr_sum = 0
            curr_sum += l1.val if l1 else 0
            curr_sum += l2.val if l2 else 0
            print(curr_sum, carry, l1.val, l2.val)
            if curr_sum > 9:
                carry = curr_sum//10
            curr_sum = curr_sum%10
            curr.next = ListNode(curr_sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry>0:
            curr.next = ListNode(carry)
    
        return dummy.next