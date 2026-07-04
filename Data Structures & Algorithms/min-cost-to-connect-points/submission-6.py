class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited, hp = set(), [(0, tuple(points[0]))]
        # visited.add(tuple(points[0]))
        ans = 0
        while len(visited) != len(points):
            # print(hp, ans)
            edge, node = heapq.heappop(hp)
            if node in visited: continue
            visited.add(node)
            ans += edge
            for x, y in points:
                if (x, y) in visited: continue
                curr_distance = abs(x - node[0]) + abs(y - node[1])
                heapq.heappush(hp, (curr_distance, (x, y)))
        return ans