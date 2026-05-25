# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        curr = head
        next = head.next

        while curr:
            if curr == next:
                return True
            curr = curr.next
            next = next.next.next if (next and next.next) else None
        return False