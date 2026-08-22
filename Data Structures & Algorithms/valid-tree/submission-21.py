class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(curr, parent):
            visited.add(curr)
            for nei in graph[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, curr): return False
            return True    
        dfs(0, -1)
        return len(visited)==n