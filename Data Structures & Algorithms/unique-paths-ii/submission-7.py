class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0
        dp = [[0] * (n) for _ in range(m)]
        for i in range(n-2, -1, -1):
            if obstacleGrid[m-1][i] == 1:
                break
            dp[m-1][i] = 1
        
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                break
            dp[i][n-1] = 1
        
        print(dp)
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if obstacleGrid[r][c] == 1: continue
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]

        
            

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