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
                # print('after end of k', curr.val)
                prev, temp = None, prev_start.next
                i = 0
                while prev!=curr:
                    # print('reversing', temp.val)
                    i += 1
                    temp_two = temp.next
                    temp.next = prev
                    prev = temp
                    temp = temp_two
                print(prev.val, prev_start.val)
                next_start = prev_start.next
                prev_start.next = prev
                next_start.next = temp
                # print(temp.val)
                curr = prev_start = next_start
                # print('post reversing', prev.val)
        return dummy.next
