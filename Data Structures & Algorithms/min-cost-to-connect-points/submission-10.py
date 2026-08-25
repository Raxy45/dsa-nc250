class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hp = [(0, 0)]
        visited = set()
        ans = 0
        while hp:
            curr_dist, popped_idx = heapq.heappop(hp)
            if popped_idx in visited: continue
            visited.add(popped_idx)
            ans += curr_dist
            for i, [x, y] in enumerate(points):
                if i in visited: continue
                heapq.heappush(hp, (abs(x-points[popped_idx][0]) + abs(y-points[popped_idx][1]), i))
        return ans
