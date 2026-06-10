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
            new_node = Node(curr.val)
            node_map[curr] = new_node
            for neighbour in curr.neighbors:
                q.append(neighbour)
                
        q = deque([node])
        curr = None
        visited = set()
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            copied_node = node_map[curr]
            visited.add(curr)
            for neighbour in curr.neighbors:
                print('adding neighbor', neighbour.val,'to', copied_node.val, 'neighbors')
                copied_node.neighbors.append(node_map[neighbour])
                q.append(neighbour)
        return node_map[node]
            
            

        