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

        count = 1
        curr = head
        prev = dummy
        while True and curr:
            count = 1 
            while count<k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1
            print('reverse right?')
            self.print_nodes(curr)
            # print(f'{curr = }')
            # print(f'{count = }')
            print(curr.val)
            print(count)
            if count == k:
                # reversed list needs to be joined
                next_group_start = curr.next
                print(f'{next_group_start = }')
                next_group_prev_pointer = start.next
                print(f'{next_group_prev_pointer.val = }')

                start.next.next = next_group_start
                start.next = curr
                curr = next_group_start
                start = next_group_prev_pointer
            self.print_nodes(dummy)
        return dummy.next