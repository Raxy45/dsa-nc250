# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        
        merged_list = []
        while len(lists)>1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list_01 = lists[i]
                if (i+1)<len(lists):
                    list_02 = lists[i+1]
                else:
                    list_02 = None
                consolidated_sorted_list = self.merge_two_list(list_01, list_02)
                merged_lists.append(consolidated_sorted_list)
            lists = merged_lists
        
        return lists[0]

    def merge_two_list(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

    def mergeKListsMe(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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

        