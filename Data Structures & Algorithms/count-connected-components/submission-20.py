class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.n = n
                self.parent = [i for i in range(n)]
                self.rank = defaultdict(int)
            

            def find(self, node):
                if node!=self.parent[node]:
                    self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu==pv:
                    return
                
                self.n -= 1
                ru, rv = self.rank[pu], self.rank[pv]
                if ru>rv:
                    self.parent[pu] = pv
                    self.rank[rv] += 1
                else:
                    self.parent[pv] = pu
                    self.rank[ru] += 1

        
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.n