# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        total_len = 0
        curr = head
        while curr:
            curr = curr.next
            total_len += 1
        # print(total_len)

        required_half = total_len //2
        curr, curr_count = head, 0
        while curr_count < required_half-1:
            curr = curr.next
            curr_count += 1
        # print(curr.val)
        
        half = curr
        prev = None
        curr = curr.next
        # print(curr.val, 'c')
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        print(prev.val)
        half.next=None
        c1, c2 = head, prev
        # print(c1.val, c2.val)
        # return
        while c1 and c2:
            t1, t2 = c1.next, c2.next
            c1.next = c2
            c1 = t1
            c2.next = c1 if c1 else c2.next
            c2 = t2
        # print(c1, c2)
