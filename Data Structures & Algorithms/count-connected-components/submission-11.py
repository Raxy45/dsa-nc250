class DSU:
    def __init__(self, n):
        self.parent = [-1] * (n)
        for i in range(n):
            self.parent[i] = i
        print(self.parent, 'pp')
        self.degree = {i: 0 for i in range(n)}
        self.components = n

    def get_parent(self, u):
        curr = self.parent[u]
        while self.parent[u] != curr:
            print(u, self.parent[u], self.parent)
            self.parent[u] = self.get_parent(self.parent[u])
            curr = self.parent[u]
        # print('parent is', curr)
        return self.parent[u]

    def union(self, u, v):
        # print('Taking union of', u, v)
        pu, pv = self.get_parent(u), self.get_parent(v)
        if pu == pv:
            return False
        
        if self.degree[pv] > self.degree[pu]:
            self.parent[pu] = pv
            self.degree[pv] += 1
        else:
            self.parent[pv] = pu
            self.degree[pu] += 1
        # print('After union', self.parent, self.degree)
        self.components -= 1
        return True

class Solution:
    def countComponents(self, n, edges):
        dsu = DSU(n)
        ans = 0
        for u, v in edges:
            dsu.union(u, v)
        
        parent = set([])
        print(dsu.parent)
        return dsu.components
    def countComponentsFirst(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        for u, v in edges:
            if u not in visited and v not in visited:
                components += 1
            visited.add(u)
            visited.add(v)
        for i in range(n):
            if i not in visited:
                components += 1
        return components