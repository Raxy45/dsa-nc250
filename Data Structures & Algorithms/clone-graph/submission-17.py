"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        if not node: return None
        q = deque([node])
        curr = None
        while q:
            curr = q.popleft()
            if curr in node_map: continue
            node_map[curr] = Node(curr.val)
            for nei in curr.neighbors:
                if nei in node_map:
                    node_map[curr].neighbors.append(node_map[nei])
                    node_map[nei].neighbors.append(node_map[curr])
                    continue
                q.append(nei)
        return node_map[node]
        