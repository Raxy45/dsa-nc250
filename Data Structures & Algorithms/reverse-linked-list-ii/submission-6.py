# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        count, curr = 1, head
        while count < left:
            prev = curr
            curr = curr.next
            count += 1
        
        prev_02 = None
        print('curr', curr.val)
        while left<=right:
            temp = curr.next
            curr.next = prev_02
            prev_02 = curr
            curr = temp
            left += 1
        
        prev.next.next = curr
        prev.next = prev_02
        return dummy.next
        
        dummy = ListNode(-1, head)
        left_previous, curr = dummy, head
        count = 1
        # 1. taking curr node to left node
        while count < left:
            left_previous = curr
            curr = curr.next
            count += 1
        # left_previous -> points to left -  1 node
        # curr -> points to beginning of element in list to be reversed
        
        prev = None
        # 2. reversing the list
        while left <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left += 1
        # curr -> points to right + 1 node
        # prev -> points to last element of sub list which needs to be reversed

        # 3. changing pointers
        # left_previous.next.next -> still points to beginning of element in list to be reversed
        left_previous.next.next = curr
        left_previous.next = prev
        return dummy.next
        
    