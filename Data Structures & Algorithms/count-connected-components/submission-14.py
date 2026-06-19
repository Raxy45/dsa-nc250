class DSU:
    def __init__(self, n):
        self.parent = [-1] * (n)
        for i in range(n):
            self.parent[i] = i
        print(self.parent, 'pp')
        self.degree = {i: 0 for i in range(n)}
        self.components = n

    def get_parent(self, u):
        if self.parent[u] != u:
            # TILL the node is not parent of itself
            # Go on processing it
            self.parent[u] = self.get_parent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.get_parent(u), self.get_parent(v)
        if pu == pv:
            return False
        
        if self.degree[pv] > self.degree[pu]:
            self.parent[pu] = pv
            self.degree[pv] += 1
        else:
            self.parent[pv] = pu
            self.degree[pu] += 1
        self.components -= 1
        return True

class Solution:
    def countComponentsDSU(self, n, edges):
        dsu = DSU(n)
        ans = 0
        for u, v in edges:
            dsu.union(u, v)
        
        print(dsu.parent)
        return dsu.components
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        graph  = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(u):
            if u in visited: return
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components