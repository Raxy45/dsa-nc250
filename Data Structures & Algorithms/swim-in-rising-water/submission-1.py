class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        hp = [(0, 0, 0)]
        visited = set()
        R, C = len(grid), len(grid[0])
        while hp:
            current_water_max, r, c = heapq.heappop(hp)
            if r==R-1 and c == C-1:
                return current_water_max
            visited.add((r, c))
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ur, uc = r + dr, c + dc
                if min(ur, uc) < 0 or ur==R or uc == C:
                    continue
                if (ur, uc) in visited: continue
                heapq.heappush(hp, (max(current_water_max, grid[ur][uc]), ur, uc))

        