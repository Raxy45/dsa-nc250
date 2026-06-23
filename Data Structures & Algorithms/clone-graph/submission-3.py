"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        node_map = {}
        c = 0
        q = deque([node])
        while q:
            c_node = q.popleft()
            node_map[c_node] = Node(c_node.val)
            for neighbor in c_node.neighbors:
                if neighbor not in node_map:
                    q.append(neighbor)
        print(node_map)
        for c_node in node_map:
            copied_node = node_map[c_node]
            for neighbor in c_node.neighbors:
                copied_node.neighbors.append(node_map[neighbor])
        return node_map[node]
