class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [float('inf')] * len(points)

        hp = [[0, 0]]
        visited = set()
        ans = 0
        while hp:
            print(hp, dist)
            curr_dist, point_idx = heapq.heappop(hp)
            if point_idx in visited:
                continue

            ans += curr_dist
            visited.add(point_idx)
            for j in range(1, len(points)):
                # print(points[j])
                if j==point_idx and j in visited: continue
                curr_delta_dist = abs(points[j][0] - points[point_idx][0]) + abs(points[j][1] - points[point_idx][1])
                if dist[j] > curr_delta_dist:
                    dist[j] = curr_delta_dist
                    heapq.heappush(hp, (curr_delta_dist, j))
        print(dist)
        # ans = 0
        # for i in dist[1:]:
        #     ans += i
        return ans