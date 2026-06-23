class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, n):
        curr = n
        while curr != self.parent[curr]:
            curr = self.parent[curr]
        return curr
    
    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u == p_v:
            # Both u and v have the same parents -> merge not required
            return False

        # we have to merge, find the bigger tree
        if self.rank[p_v] > self.rank[p_u]:
            p_u, p_v = p_v, p_u
        
        self.parent[p_v] = p_u
        self.rank[p_u] += self.rank[p_v]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res