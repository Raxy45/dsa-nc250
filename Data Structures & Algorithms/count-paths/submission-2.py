class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsRecWithMemo(self, m: int, n: int) -> int:
        dp = [[-1]*(n) for _ in range(m)]
        dp[m-1][n-1] = 1
        ans = 0
        def solve(r, c):
            nonlocal ans
            if r == m or c==n or min(r,c) < 0:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            curr = 0
            curr += solve(r+1, c)
            curr += solve(r, c+1)
            dp[r][c] = curr
            return curr
        return solve(0, 0)