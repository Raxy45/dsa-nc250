# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n==1:
            return None
        slow = ListNode(0, head)
        fast = head
        i = 0
        while i<n:
            fast = fast.next
            i += 1
        
        # if not fast:
        #     # meaning n was same as length of linked list length, therefore we have
        #     # to remove the element from beginning of list. example [1,2,3] n = 3
        #     head = head.next
        while fast:
            fast = fast.next
            slow = slow.next
        # print(slow.val, fast.val)
        slow.next = slow.next.next
        return head

    
        ll_length = 0
        temp = head
        while temp:
            temp = temp.next
            ll_length += 1
        
        if ll_length<=1:
            return None
        required_node = ll_length-n
        if required_node==0:
            head=head.next
        else:
            temp = head
            i = 1
            while i<required_node:
                temp = temp.next
                i += 1
            if temp.next:
                temp.next = temp.next.next
            else:
                temp.next=None
        return head