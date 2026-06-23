# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = ListNode(0,head)
        fast = head.next

        while slow and fast:
            if slow == head: return True
            slow = slow.next
            fast = fast.next
        return False