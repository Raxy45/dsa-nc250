# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left_previous, curr = dummy, head
        count = 1
        while count < left:
            left_previous = curr
            curr = curr.next
            count += 1
        
        prev = None
        while left <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left += 1
        
        left_previous.next.next = curr
        left_previous.next = prev
        return dummy.next

        reverse_from_begin = False
        if left == 1:
            reverse_from_begin = True
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
        print('left_start', head.val)

        # reverse list
        prev = before
        while left<=right:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            left += 1
            # print('left', left)
        print('before ', before.val)
        print('prev', prev.val)
        print('before.next.val', before.next.val)
        before.next.next = head
        before.next = prev
        if reverse_from_begin:
            return prev
        return start
        # after = head.next # points to right + 1
        # print('after rr', after.val)
        # left_start = before.next
        # print('left_start ', left_start.val)
        # print('right_end ', head.val)
        # print()
        # before.next = head
        # left_start.next = after
        return start
        # print(start.val, left_start.val)
        return start
        
    