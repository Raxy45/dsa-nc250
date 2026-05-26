# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_start = ListNode(0, head)
        curr = dummy
        while curr:
            count = 0
            # print('starting new journey from', curr.val)
            while count < k and curr:
                curr = curr.next
                count += 1
            

            if curr:
                prev, temp = None, prev_start.next
                while prev!=curr:
                    temp_two = temp.next
                    temp.next = prev
                    prev = temp
                    temp = temp_two
                next_start = prev_start.next
                prev_start.next = prev
                next_start.next = temp
                curr = prev_start = next_start
        return dummy.next
