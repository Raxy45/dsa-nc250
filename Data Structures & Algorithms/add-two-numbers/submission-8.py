# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_h = tail_h = ListNode()
        carry = 0
        while l1 and l2:
            n1 = l1.val
            n2 = l2.val
            curr_num = n1+n2+carry
            print('c_num', curr_num)
            carry = curr_num//10
            curr_num = curr_num%10
            print('carry', carry)
            print('c_num', curr_num)  
            curr_node = ListNode(curr_num)
            tail_h.next = curr_node
            tail_h = tail_h.next
            l1 = l1.next
            l2 = l2.next
        
        temp = ans_h.next
        while temp:
            print(temp.val)
            temp = temp.next
        print('b4')
        while l1:
            print('l1 exists')
            n1 = l1.val
            curr_num = n1 + carry
            carry = curr_num//10
            curr_num = curr_num%10
            curr_node = ListNode(curr_num)
            tail_h.next = curr_node
            tail_h = tail_h.next
            l1 = l1.next
        
        l1 = l2
        while l1:
            print('l2 exists')
            n1 = l1.val
            curr_num = n1 + carry
            if curr_num> 9:
                carry = curr_num//10
                curr_num = curr_num%10
            curr_node = ListNode(curr_num)
            tail_h.next = curr_node
            tail_h = tail_h.next
            l1 = l1.next

        if carry>0:
            curr_node = ListNode(carry)
            tail_h.next = curr_node
        temp = ans_h.next
        while temp:
            print(temp.val)
            temp = temp.next
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
