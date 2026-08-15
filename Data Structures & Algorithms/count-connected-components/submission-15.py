class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.n = n
                self.rank = [0] * n

            def get_parent(self, node):
                if node != self.parents[node]:
                    self.parents[node] = self.get_parent(self.parents[node])
                return node

            def union(self, u, v):
                pu, pv = self.get_parent(u), self.get_parent(v)
                if pu == pv:
                    return
                
                ru, rv = self.rank[pu], self.rank[pv]
                if ru > rv:
                    self.parents[pv] = pu
                    self.rank[pu] += 1
                else:
                    # rv >= ru
                    self.parents[pu] = pv
                    self.rank[pv] += 1
                self.n -= 1

        dsu = DSU(n)
        for n1, n2 in edges:
            dsu.union(n1, n2)
        return dsu.n