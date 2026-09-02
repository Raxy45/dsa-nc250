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
            
        node_map = {node:Node(node.val)}
        def dfs(node):
            if not node:
                return None

            new_node = Node(node.val)
            node_map[node] = new_node
            for nei in node.neighbors:
                if nei not in node_map:
                    dfs(nei)
                new_node.neighbors.append(node_map[nei])
            return new_node
        return dfs(node)

        
        if not node:
            return
            
        node_map = {node:Node(node.val)}
        
        
        c = 0
        q = deque([node])
        while q:
            c_node = q.popleft()
            for neighbor in c_node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                node_map[c_node].neighbors.append(node_map[neighbor])
                # else:
                #     node_map[c_node].neighbors.append(node_map[neighbor])

        # for c_node in node_map:
        #     copied_node = node_map[c_node]
        #     for neighbor in c_node.neighbors:
        #         copied_node.neighbors.append(node_map[neighbor])
        return node_map[node]
