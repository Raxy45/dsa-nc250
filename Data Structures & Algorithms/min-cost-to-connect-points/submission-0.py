class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        m = [float('inf')] * len(points)
        print(m)

        m[0] = 0
        # for i in range(len(points)):
        #     x, y = points[i]
        #     for j in range(len(points)):
        #         if i==j: continue
        #         updated_dist = abs(points[j][0]-x) + abs(points[j][1]-y)
        #         if m[j] > updated_dist:
        #             m[j] = updated_dist
        # print(m)

        hp = [[0, points[0]]]
        visited = set()
        while hp:
            curr_dist, [x, y] = heapq.heappop(hp)
            visited.add((x,y))
            for i in range(len(points)):
                dx, dy = points[i][0], points[i][1]
                if dx==x and dy==y or (dx, dy) in visited: continue

                dist = abs(dx-x) + abs(dy-y)
                if m[i] > dist:
                    m[i] = dist
                    heapq.heappush(hp, [dist, points[i]])
        return sum(m)