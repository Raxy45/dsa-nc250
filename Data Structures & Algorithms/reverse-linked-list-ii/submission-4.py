# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left_previous, curr = dummy, head
        count = 1
        while count < left:
            left_previous = curr
            curr = curr.next
            count += 1
        
        prev = None
        while left <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left += 1
        
        left_previous.next.next = curr
        left_previous.next = prev
        return dummy.next
        
    