# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = dummy = ListNode(next=head)
        count = 0
        while count != n:
            curr = curr.next
            count += 1
        
        slow = dummy
        print(curr.val, slow.val)
        while curr.next:
            curr = curr.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
