class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        ans = []
        def dfs(curr):
            while graph[curr]:
                nei = graph[curr].pop(0)
                dfs(nei)
            ans.append(curr)
        dfs('JFK')
        return ans[::-1]            

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        
        cities = ['JFK']
        def dfs(curr):
            if len(cities) == len(tickets) + 1: return True
            curr_neis = graph[curr]
            for i, nei_city in enumerate(curr_neis):
                cities.append(nei_city)
                curr_neis.remove(nei_city)

                if dfs(nei_city): return True

                curr_neis.insert(i, nei_city)
                cities.pop()
            return False
        dfs('JFK')
        return cities

