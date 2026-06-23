# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = ListNode(0, head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev_start = slow

        prev = None
        curr = slow.next
        prev_start.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start1, start2 = head, prev
        print(start1.val, start2.val)
        # return
        while start1 and start2:
            temp1, temp2 = start1.next, start2.next
            start1.next = start2
            start2.next = temp1 if temp1 else temp2
            start1, start2 = temp1, temp2