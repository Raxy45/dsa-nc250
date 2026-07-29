class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]
        # print(dp)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # print('i, j', i, j)
                if (i+1) < m:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                
                if (j+1) < n:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])
                # print(dp)
            # print()
        return dp[0][0]