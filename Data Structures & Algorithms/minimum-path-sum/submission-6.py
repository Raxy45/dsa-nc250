class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n) for _ in range(m)]
        curr = [float('inf')] * (n)
        curr[n-1] = grid[m-1][n-1]
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i+1) < m:
                    curr[j] = grid[i][j] + curr[j]
                
                if (j+1) < n:
                    curr[j] = min(curr[j], grid[i][j] + curr[j+1])
        return curr[0]