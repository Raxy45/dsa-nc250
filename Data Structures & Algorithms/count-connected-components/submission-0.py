class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(v):
            visit.add(v)
            if graph[v] == []:
                return
            
            for child in graph[v]:
                if child not in visit:
                    dfs(child)

        count = 0
        for v in range(n):
            if v not in visit:
                dfs(v)
                count += 1
        return count