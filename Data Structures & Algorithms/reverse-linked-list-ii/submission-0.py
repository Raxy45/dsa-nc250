# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        before = ListNode(-1)
        before.next=head
        after = None
        count = 1
        while count<left:
            before = head
            head = head.next
            count += 1
        # before -> points to left -1 
        print('before rr', before.val)

        # reverse list
        prev = before
        while left<right:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            left += 1
            print('left', left)
        after = head.next # points to right + 1
        print('after rr', after.val)
        left_start = before.next
        print('left_start ', left_start.val)
        print('right_end ', head.val)
        print()
        before.next = head
        left_start.next = after
        return start
        # print(start.val, left_start.val)
        return start
        
    