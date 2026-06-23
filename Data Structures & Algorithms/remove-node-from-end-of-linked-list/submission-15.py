# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = root = ListNode(0, head)
        count = 0
        fast = head
        while count < n-1:
            fast = fast.next
            count += 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return root.next