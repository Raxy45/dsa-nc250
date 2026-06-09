class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        ans = 0
        def dfs(r, c):
            if (r, c) in visited: return 0
            nonlocal ans
            if r<0 or r==R or c<0 or c==C:
                return 1

            if grid[r][c] == 0:
                return 1
            
            visited.add((r, c))
            rhs = dfs(r, c+1)
            lhs = dfs(r, c-1)
            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            ans += rhs + lhs + bottom + top
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        return ans