class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = set()
        for [v1, v2] in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
