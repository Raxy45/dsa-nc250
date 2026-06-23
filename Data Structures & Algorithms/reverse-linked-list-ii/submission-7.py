# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = curr = ListNode(next=head)
        count = 0
        while count+1<left:
            curr = curr.next
            count += 1
        print(curr.val)
        
        slow2 = curr
        prev = None
        diff = left
        new_end = curr = curr.next
        print(slow2.val, curr.val)
        while diff<=right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            diff += 1
        slow2.next = prev
        new_end.next = curr
        return dummy.next
        # while (right)