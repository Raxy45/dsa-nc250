class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r<0 or r==R or c<0 or c==C or (r,c) in visited or grid[r][c]==0:
                return 0
            
            area = 1

            visited.add((r, c))
            area += solve(r, c+1)
            area += solve(r+1, c)
            area += solve(r, c-1)
            area += solve(r-1, c)
            return area
        
        R, C = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1 and (r, c) not in visited:
                    max_area = max(max_area, solve(r, c))
        return max_area