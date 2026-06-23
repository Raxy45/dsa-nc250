class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        ans = []
        def dfs(var_to_match, current_node):
            nonlocal i
            if i>10:
                return None, None
            i += 1
            print('iterating over', current_node, 'to find match for', var_to_match)
            for nei in graph[current_node]:
                nei_node, nei_value = nei
                if nei_node == var_to_match:
                    return nei_node, nei_value
                matched_nei, matched_nei_val = dfs(var_to_match, nei_node)
                if not matched_nei:
                    continue
                else:
                    return matched_nei, matched_nei_val
            return None, None
        for qv1, qv2 in queries:
            print('Current Query', qv1, qv2)
            if qv1 not in graph or qv2 not in graph:
                print('qv1 or qv2 not found in graph, adding -1')
                ans.append(-1)
                continue
            found_match = False
            for var, val in graph[qv1]:
                print('finding a match for', var, val, 'in nei of', qv2)
                if var == qv2:
                    # direct mapping exists
                    ans.append(val)
                    found_match = True
                    break
                matched, matched_value = dfs(var, qv2)
                if not matched:
                    continue
                if matched:
                    ans.append(val/matched_value)
                    found_match = True
                    break
            if not found_match:
                ans.append(-1)
            print(ans,'for', qv1, qv2)
        return ans
                
