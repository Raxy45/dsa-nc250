class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit: return False

            visit.add(i)
            for child in adj[i]:
                if child == prev: continue
                if not dfs(child, i): return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n