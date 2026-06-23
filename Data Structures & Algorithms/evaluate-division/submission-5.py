class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        ans = []
        def dfs(current, target, visited):
            if current not in graph or target not in graph:
                return -1
            if current == target: return 1
            visited.add(current)
            for current_nei_var, current_nei_val in graph[current]:
                if current_nei_var in visited:
                    continue
                match = dfs(current_nei_var, target, visited)
                if match != -1:
                    return current_nei_val * match
            return -1
        for src, dest in queries:
            found_match = False
            for nei_var, nei_val in graph[src]:
                match = dfs(nei_var, dest, set())
                if match == -1:
                    continue
                ans.append(nei_val * match)
                found_match = True
                break
            if not found_match:
                ans.append(-1)
        return ans

            
            
        
                

            
            
        
                
