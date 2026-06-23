class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        max_area = 0
        def dfs(r, c):
            if r<0 or r==R or c<0 or c==C or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            area = 0
            visited.add((r, c))
            area += 1
            area += dfs(r, c+1)
            area += dfs(r+1, c)
            area += dfs(r, c-1)
            area += dfs(r-1, c)
            print('area returned by',r,c,'is',area)
            return area
        
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    print('New island: ',r,c)
                    area_new_i = dfs(r, c)
                    print('area returned by new island', area_new_i)
                    max_area = max(max_area, area_new_i)
        return max_area
