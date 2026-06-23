class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r<0 or r==R or c<0 or c==C:
                return 1
            
            if grid[r][c] == 0:
                return 1

            if (r, c) in visited: return 0

            visited.add((r, c))
            exploration = dfs(r, c+1) + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1, c)
            visited.remove((r, c))
            return exploration
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0