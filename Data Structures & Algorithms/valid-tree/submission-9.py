class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        print(n, edges)
        if len(edges)!=n-1: return False
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        print(graph)
        visited = set()
        def dfs(idx, prev):
            if idx in visited:
                return False
            
            visited.add(idx)
            for v in graph[idx]:
                if v!=prev and not dfs(v, idx): return False
            return True

        dfs(0, -1)
        return len(visited)==n
