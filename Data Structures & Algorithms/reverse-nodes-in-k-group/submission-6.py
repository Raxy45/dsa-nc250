# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy
        prev = None
        curr = head
        while curr:
            count = 0
            while count<k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1
            if count==k:
                # We first need to store next group beginning - 1 pointer
                next_group_start_minus_1=start.next

                # Now we just update the pointers of left node and right node of group
                start.next.next = curr
                start.next = prev

                # store the next group beginning minus one pointer in start
                start = next_group_start_minus_1
                prev = None
            else:
                # Undo the reversing
                curr = prev
                prev = None
                while curr:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
        return dummy.next