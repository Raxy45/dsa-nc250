# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print('okay')
        # return
        print(slow.val)
        # return
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        print('in here')
        # return
        start1 = head
        start2 = prev
        print(start1.val, start2.val)
        # return
        curr = start2
        while curr:
            print(curr.val, '->')
            curr = curr.next
        print('post')
        print(start1.val, start2.val)
        while start1 and start2:
            temp1 = start1.next
            temp2 = start2.next
            start1.next = start2
            start2.next = temp1
            start1 = temp1
            start2 = temp2
        # return head