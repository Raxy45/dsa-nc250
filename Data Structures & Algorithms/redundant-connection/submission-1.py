class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            
            def find(self, node):
                curr = node
                if curr == self.parent[curr]:
                    return curr
                
                self.parent[curr] = self.find(self.parent[curr])
                return self.parent[curr]
            
            def union(self, u, v):
                p_u, p_v = self.find(u), self.find(v)
                if p_u == p_v:
                    return False
                
                r_u, r_v = self.rank[p_u], self.rank[p_v]
                if r_u > r_v:
                    self.parent[p_v] = p_u
                elif r_v>r_u:
                    self.parent[p_u] = p_v
                else:
                    self.parent[p_u] = p_v
                    self.rank[p_v] += 1
                return True
            
        dsu = DSU(len(edges)+1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]