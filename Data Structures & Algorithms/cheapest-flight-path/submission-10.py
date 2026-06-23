from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)

        for u, v, cost in flights:
            graph[u].append((v, cost))

        dist = [float('inf')] * n
        dist[src] = 0

        q = deque([(src, 0)])  # (node, cost)
        level = 0

        while q and level <= k:
            size = len(q)

            # Important: use a copy to avoid same-level updates affecting current level
            temp_dist = dist.copy()

            for _ in range(size):
                node, curr_cost = q.popleft()

                for nei, price in graph[node]:
                    if curr_cost + price < temp_dist[nei]:
                        temp_dist[nei] = curr_cost + price
                        q.append((nei, curr_cost + price))

            dist = temp_dist
            level += 1

        return -1 if dist[dst] == float('inf') else dist[dst]