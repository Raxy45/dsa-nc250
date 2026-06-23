# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prefix = dummy = ListNode(0, head)
        while prefix.next.val != left:
            prefix = prefix.next
        
        suffix = prefix
        while suffix.val != right:
            suffix = suffix.next
        
        suffix = suffix.next
        # print(prefix.val, suffix.val)
        prev, curr = None, prefix.next
        while curr!=suffix:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # print(prev.val)
        prefix.next.next = suffix
        prefix.next = prev
        return dummy.next

        
