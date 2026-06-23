class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(0)

        return len(visited) == n