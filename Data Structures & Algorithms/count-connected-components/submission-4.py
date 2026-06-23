class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(idx):
            if idx in visited: return
            visited.add(idx)
            if len(graph[idx])==0: return

            for edge in graph[idx]:
                dfs(edge)
        
        visited = set()
        count = 0
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
                count += 1
        return count