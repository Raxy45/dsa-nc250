class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Graph is valid tree iff:
        # 1. Number of edges == n-1
        # 2. Graph is connected
        # 3. All the nodes are connected

        # Both 1 and 2 automatically guarantees, we dont get a cycle
        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            # graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(0)
        return len(visited) == n