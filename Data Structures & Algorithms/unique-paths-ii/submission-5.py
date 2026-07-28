class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0
        dp = {(m-1, n-1): 1}
        def dfs(r, c):
            if (r, c) in dp: return dp[(r, c)]
            if min(r, c) < 0 or r==m or c==n or obstacleGrid[r][c] == 1: return 0
            dp[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
            return dp[(r, c)]
        return dfs(0, 0)