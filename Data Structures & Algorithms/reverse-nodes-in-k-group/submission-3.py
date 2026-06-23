# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_nodes(self, node):
        while node:
            print(node.val, '->')
            node = node.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = start = ListNode(0, head)
        prev =  None
        count = 0
        curr = head
        while curr:
            count = 0
            while count<k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1
            if count==k:
                next_group_start = start.next
                start.next.next = curr
                start.next = prev
                start = next_group_start
                prev = None
            else:
                # reverse the remainder list
                curr = prev
                prev = None
                while curr:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
        return dummy.next

