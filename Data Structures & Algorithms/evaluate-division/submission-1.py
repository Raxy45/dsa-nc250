class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, e in enumerate(equations):
            v1, v2 = e
            graph[v1].append([v2, values[idx]])
            graph[v2].append([v1, 1/values[idx]])
        
        def dfs(src, target, visited):
            print(src, target)
            if src not in graph or target not in graph:
                return -1
            
            if src == target: return 1

            visited.add(src)
            for node, current_wt in graph[src]:
                print(node, 'is',current_wt)
                if node in visited: continue
                wt = dfs(node, target, visited)
                if wt==-1: return -1
                return current_wt * wt
            return -1
        
        ans = []
        for query in queries:
            src, target = query[0], query[1]
            ans.append(dfs(src, target, set()))
        return ans