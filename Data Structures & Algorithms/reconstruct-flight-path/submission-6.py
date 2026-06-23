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
            if city not in graph or len(ans)==len(tickets)+1: return
            
            print(city, graph[city])
            print(ans)
            temp = graph[city].copy()
            for i in range(len(temp)):
                if len(ans) == len(tickets)+1: continue
                ans.append(temp[i])
                graph[city].pop(i)

                dfs(temp[i])

                graph[city].insert(i, temp[i])
        dfs('JFK')
        return ans