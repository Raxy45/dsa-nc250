# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = root = ListNode(0, head)
        count = 1
        fast = head
        while count < n:
            fast = fast.next
            count += 1
        print(fast.val)
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return root.next