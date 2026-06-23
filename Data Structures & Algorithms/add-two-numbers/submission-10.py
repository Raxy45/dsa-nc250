# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_h = tail_h = ListNode()
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            curr_num = n1+n2+carry
            carry = curr_num//10
            curr_num = curr_num%10
            curr_node = ListNode(curr_num)
            tail_h.next = curr_node
            tail_h = tail_h.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry>0:
            curr_node = ListNode(carry)
            tail_h.next = curr_node
        return ans_h.next
        num1 = 0
        multiply = 1
        head1 = l1
        while head1:
            num1 = head1.val*multiply + num1
            multiply = multiply*10
            head1 = head1.next

        head1 = l2
        num2, multiply = 0, 1
        while head1:
            num2 = head1.val*multiply + num2
            multiply = multiply*10
            head1 = head1.next
        ans = num1+num2
        if ans == 0:
            return ListNode(0)
        ans_h = tail = ListNode()
        while ans:
            curr_val = ans%10
            curr_node = ListNode(curr_val)
            tail.next = curr_node
            tail = tail.next
            ans = ans//10
        return ans_h.next
