class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Build Graph
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = set()
        def dfs(idx, prev):
            if idx in visited:
                # when we get a node, which is not its parent but is 
                # already visited, then in such cases we return False
                return False
            
            visited.add(idx)
            for v in graph[idx]:
                if v==prev:
                    # we go from 0 to 1, then in 1 we will also have 0
                    # but let us not travel 0, as we are coming from there
                    continue
                
                if not dfs(v, idx): return False
            return True

        return dfs(0, -1) and len(visited)==n
