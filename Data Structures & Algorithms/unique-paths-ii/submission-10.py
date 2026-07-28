class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * (N + 1)
        dp[N - 1] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c + 1]

        return dp[0]

        
            

    def uniquePathsWithObstaclesT(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0
        dp = {(m-1, n-1): 1}
        def dfs(r, c):
            if (r, c) in dp: return dp[(r, c)]
            if min(r, c) < 0 or r==m or c==n or obstacleGrid[r][c] == 1: return 0
            dp[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
            return dp[(r, c)]
        return dfs(0, 0)