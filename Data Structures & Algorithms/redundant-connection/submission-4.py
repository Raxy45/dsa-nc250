class DSU:
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.parent = [i for i in range(n+1)]

    def get_parent(self, u):
        if u!=self.parent[u]:
            self.parent[u] = self.get_parent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.get_parent(u), self.get_parent(v)
        if pu == pv:
            # already u and v belong to same group,
            # no need for edge connection from u to v 
            return True
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if dsu.union(u, v):
                return [u, v]
        