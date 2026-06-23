# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val<c2.val:
                tail.next=c1
                c1 = c1.next
            else:
                tail.next = c2
                c2 = c2.next
            tail = tail.next
        
        if c1:
            tail.next = c1
        if c2:
            tail.next = c2
        
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        while len(lists)>1:
            list1, list2 = None, None
            current_length = len(lists)
            merged_lists = []
            for i in range(0, current_length-1,2):
                print(i)
                list1 = lists[i]
                list2 = lists[i+1]
                merged_list = self.mergeTwoLists(list1, list2)
                merged_lists.append(merged_list)
            if (current_length%2)>0:
                merged_lists.append(lists[current_length-1])
            print('***')
            lists = merged_lists
        return lists[0]
