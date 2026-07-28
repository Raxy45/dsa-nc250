class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            dp[i][n-1] = 1

        for i in range(n):
            dp[m-1][i] = 1

        # print(dp)
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]
        