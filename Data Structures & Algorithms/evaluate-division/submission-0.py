class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # We build a graph for each variable in below form
        # a -> (b, value) i.e. numerator -> (denominator, value)
        # Also, we will need to store the relation from denominator to numerator
        # b -> (a, 1/value)

        graph = defaultdict(list)
        for i, variables in enumerate(equations):
            graph[variables[0]].append((variables[1], values[i]))   # a -> (b, val)
            graph[variables[1]].append((variables[0], 1/values[i])) # b -> (a, 1/val)

        # now the graph is genarated and we will traverse for the queries in graph
        def dfs(src, target, visited):
            print(src, target)
            if src not in graph or target not in graph:
                # when either src or target, none of them exists in graph -> return -1
                return -1

            if src == target:
                # THis is the base case
                return 1

            visited.add(src) # mark current variable as visited
            current_weight = -1
            for denominator, weight in graph[src]:
                print(denominator, weight)
                if denominator not in visited:
                    current_weight = dfs(denominator, target, visited)
                
                if current_weight != -1:
                    return current_weight * weight
            return -1

        ans = []
        for query in queries:
            src, target = query[0], query[1]
            ans.append(dfs(src, target, set()))
        return ans