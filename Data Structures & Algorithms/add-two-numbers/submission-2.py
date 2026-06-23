# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
