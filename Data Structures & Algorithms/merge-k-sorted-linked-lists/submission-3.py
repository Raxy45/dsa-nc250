# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:

            list1 = lists.pop()
            list2 = lists.pop()
            merged_list = self.mergeTwoList(list1, list2)
            lists.append(merged_list)
        
        return lists