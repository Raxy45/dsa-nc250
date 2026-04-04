class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * C for _ in range(R)]
        def solve(r, c):
            if min(r, c) < 0 or r==R or c==C or obstacleGrid[r][c] == 1:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = solve(r+1, c) + solve(r, c+1)
            return dp[r][c]
            
        if obstacleGrid[R-1][C-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp[R-1][C-1] = 1 
        return solve(0, 0)