class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, tickets in flights:
            graph[u].append((v, tickets))
        
        hp = [(0, src, -1)] # tix, node, stops
        dist = [float('inf')] * n

        while hp:
            curr_tix, node, curr_k = heapq.heappop(hp)
            if curr_k == k:
                if node == dst:
                  return curr_tix
                # no point in storing nodes which have stops already equal to k
                continue
            
            for nei, tix in graph[node]:
                heapq.heappush(hp, (tix+curr_tix, nei, curr_k+1))
        return -1