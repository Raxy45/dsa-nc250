"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:    return None
        
        n_d = {}
        def solve(node):
            if node in n_d: return n_d[node]

            new_node = Node(node.val, [])
            n_d[node] = new_node

            for neighbor in node.neighbors:
                n_d[node].neighbors.append(solve(neighbor))
            return n_d[node]
        solve(node)
        return n_d[node]