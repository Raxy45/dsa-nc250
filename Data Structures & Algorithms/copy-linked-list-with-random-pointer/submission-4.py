"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        ll_hmp = {None:None}
        while curr:
            new_node = Node(curr.val)
            ll_hmp[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = ll_hmp[curr]
            new_node.next = ll_hmp[curr.next]
            new_node.random = ll_hmp[curr.random]
            curr = curr.next
        
        return ll_hmp[head]