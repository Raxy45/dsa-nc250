class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        print(graph)

        m = [float('inf') for _ in range(n)]
        m[src] = 0
        hp = [(0, src)]
        while hp:
            dist, node = heapq.heappop(hp)
            for neighbour, curr_dist in graph[node]:
                updated_dist = curr_dist + dist
                if m[neighbour] > updated_dist:
                    m[neighbour] = updated_dist
                    heapq.heappush(hp, (updated_dist, neighbour))
    
        ans = {}
        for i in range(len(m)):
            ans[i] = m[i]
            if m[i] == float('inf'):
                ans[i] = -1
        return ans
