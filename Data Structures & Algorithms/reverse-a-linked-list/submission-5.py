# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        temp = None
        while head:
            temp = head.next
            head.next=prev
            prev=head
            head=temp
        return prev

        new_head = self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new_head
        
        temp, j = None, None
        i = head
        if i is None:
            return i
        while i:
            temp = i.next
            i.next=j
            j=i
            i=temp
        return j