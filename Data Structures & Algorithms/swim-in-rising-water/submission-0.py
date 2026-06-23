class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        hp = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        c_max = 0
        while hp:
            curr_wt_level, r, c = heapq.heappop(hp)
            if (r, c) in visited:
                continue
            if r==R-1 and c==C-1:
                return curr_wt_level
            visited.add((r, c))
            for dr, dc in directions:
                ur, uc = r+dr, c+dc
                if min(ur, uc) < 0 or ur==R or uc==C or (ur, uc) in visited:
                    continue
                heapq.heappush(hp, (max(curr_wt_level, grid[ur][uc]), ur, uc))
                    
                