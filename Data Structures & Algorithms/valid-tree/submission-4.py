class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1: return False
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        print(graph)
        visited = set()
        def dfs(idx, prev):
            print('solving for',idx,prev, visited)
            if len(graph[idx]) == 0:
                return True
            
            if idx in visited and idx!=prev:
                # print('cycle detected')
                return False
            
            visited.add(idx)
            for v in graph[idx]:
                print(v, idx, prev)
                if v!=prev and not dfs(v, idx): return False
            visited.remove(idx)
            graph[idx] = []
            return True

        for i in range(len(graph)):
            if not dfs(i, i): return False
        return True
