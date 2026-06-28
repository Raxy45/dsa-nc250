class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dest in tickets:
            if src not in graph:
                graph[src] = []
            heapq.heappush(graph[src], dest)
        print(graph)
        visited = set()
        hp = ['JFK']
        ans = []
        while hp:
            curr_city = heapq.heappop(hp)
            ans.append(curr_city)
            if curr_city not in graph or len(graph[curr_city]) == 0: continue
            next_dest = heapq.heappop(graph[curr_city])
            heapq.heappush(hp, next_dest)
        return ans