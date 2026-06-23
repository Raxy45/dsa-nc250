# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        i = 0
        dummy = curr = ListNode()
        while l1 or l2 or carry:
            curr_sum = l1.val if l1 else 0
            curr_sum += l2.val if l2 else 0
            print(l1, l2, carry)
            i += 1
            if i==20:
                break
            curr_sum += carry 
            if curr_sum > 9:
                curr_sum = curr_sum%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(curr_sum)
            curr.next = new_node
            print(new_node, new_node.val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(carry)
        return dummy.next