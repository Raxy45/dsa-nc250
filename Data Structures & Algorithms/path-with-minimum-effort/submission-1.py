class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]

        m = [[float('inf') for _ in range(C)] for _ in range(R)]
        hp = [[0,0,0]]
        while hp:
            diff, r, c = heapq.heappop(hp)
            if r==R-1 and c==C-1:
                return diff
            
            for dr, dc in directions:
                ur, uc = r+dr, c+dc
                if min(ur, uc)<0 or ur==R or uc==C:
                    continue
                
                updated_diff = max(diff, abs(heights[r][c] - heights[ur][uc]))
                if updated_diff < m[ur][uc]:
                    m[ur][uc] = updated_diff
                    heapq.heappush(hp, [updated_diff, ur, uc])