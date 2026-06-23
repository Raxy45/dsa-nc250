class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        m = [[float('inf') for _ in range(C)] for _ in range(R)]
        m[0][0] = 0
        hp = [(0, 0, 0)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while hp:
            dist, r, c = heapq.heappop(hp)
            if r==R-1 and c==C-1:
                return dist
            
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if min(ur, uc) < 0 or ur==R or uc==C:
                    continue
                
                updated_dist = abs(heights[ur][uc] - heights[r][c])
                max_dist = max(dist, updated_dist)
                if m[ur][uc] >  max_dist:
                    # relax
                    m[ur][uc] = max_dist
                    heapq.heappush(hp,(max_dist, ur, uc))