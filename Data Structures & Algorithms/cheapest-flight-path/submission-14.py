class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. Build graph
        graph = {i: [] for i in range(n)}
        for csrc, cdest, cprice in flights:
            graph[csrc].append((cdest, cprice))
        print(graph)

        # 2. Add starting point to heap
        hp = [(0, -1, src)] # price, stops, current airport

        while hp:
            price, stops, curr_airport = heapq.heappop(hp)
            if curr_airport == dst: return price

            if (stops + 1) > k: continue
            for next_stop, tix_price in graph[curr_airport]:
                heapq.heappush(hp, (price+tix_price, stops+1, next_stop))
        return -1