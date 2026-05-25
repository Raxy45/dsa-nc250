# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast, c = dummy, 0
        while c<=n:
            fast = fast.next
            c += 1
        
        slow = dummy
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return dummy.next