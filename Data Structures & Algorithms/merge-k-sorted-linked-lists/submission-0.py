# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode(-1)
        idx, elem_added = None, False
        while True:
            elem_added = False
            curr_min = ListNode(sys.maxsize)
            for i in range(0, len(lists)):
                if lists[i]:
                    curr_node = lists[i]
                    if curr_node.val < curr_min.val:
                        curr_min = curr_node
                        idx = i
                        elem_added = True
            if not elem_added:
                break
            tail.next = curr_min
            lists[idx] = lists[idx].next
            tail = tail.next
        return dummy.next    

        