class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        print(graph)
        for src, cities in graph.items():
            cities.sort()
        print(graph)

        ans = ['JFK']
        def dfs(city):
            nonlocal ans
            if len(ans)==len(tickets)+1: return True
            if city not in graph: return False
            
            print(city, graph[city])
            print(ans)
            temp = graph[city].copy()
            for i in range(len(temp)):
                if len(ans) == len(tickets)+1: continue
                ans.append(temp[i])
                graph[city].pop(i)

                if dfs(temp[i]): return True

                graph[city].insert(i, temp[i])
                ans.pop()
        dfs('JFK')
        return ans