# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prefix = dummy = ListNode(0, head)
        curr = 0
        while curr<left-1:
            prefix = prefix.next
            curr += 1
        
        suffix = prefix
        while curr<right:
            suffix = suffix.next
            curr += 1
        
        suffix = suffix.next
        print(prefix.val, suffix.val)
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

        
