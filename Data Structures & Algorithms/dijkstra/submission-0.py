class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        m = [float('inf') for _ in range(n)]
        hp = [[0, 0]]
        m[0] = 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        # print(graph)

        while hp:
            dist, node = heapq.heappop(hp)

            for neighbour, curr_dist in graph[node]:
                updated_dist = curr_dist + dist
                if updated_dist<m[neighbour]:
                    heapq.heappush(hp, (updated_dist, neighbour))
                    m[neighbour] = updated_dist
        
        ans = {}
        for i in range(len(m)):
            ans[i] = m[i]
        return ans