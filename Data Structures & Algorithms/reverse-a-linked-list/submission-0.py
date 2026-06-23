# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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