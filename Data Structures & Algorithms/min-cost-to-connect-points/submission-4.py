class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = deque([points[0]])
        visited = set()
        ans = 0

        while len(visited) != len(points):
            curr_min_d, cpair = float('inf'), None
            for x, y in points:
                if not q:
                    q.append((x, y))
                    visited.add((x, y))
                    break
                if (x, y) in visited: continue
                for i in range(len(q)):
                    cx, cy = q[i]
                    if (abs(cx - x) + abs(cy-y)) < curr_min_d:
                        curr_min_d = (abs(cx - x) + abs(cy-y))
                        cpair = (x, y)
            if cpair:
                ans += curr_min_d
                visited.add(cpair)
                q.append(cpair)


        return ans