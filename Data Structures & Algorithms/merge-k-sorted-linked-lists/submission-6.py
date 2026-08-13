# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            curr = head = ListNode(None)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
                curr = curr.next
            if l2:
                curr.next = l2
                curr = curr.next
            
            return head.next
        if not lists:
            # print('here')
            return None
        q = deque(lists)
        while len(q) > 1:
            n1 = q.popleft()
            n2 = q.popleft()
            merged_list = merge(n1, n2)
            q.append(merged_list)
        print(q)
        return q[0]