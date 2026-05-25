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
        node_map = {None:None}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_node = node_map[curr]
            new_node.next = node_map[curr.next]
            new_node.random = node_map[curr.random]
            curr = curr.next
        return node_map[head]