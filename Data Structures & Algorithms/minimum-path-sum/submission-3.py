class Solution:
    def minPathSum(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [float('inf')] * C
        dp[C-1] = grid[R-1][C-1]
        for i in range(R-1, -1, -1):
            # print(i)
            for j in range(C-1, -1, -1):
                if i==R-1 and j==C-1:
                    continue
                if (j+1)<C:
                    dp[j] = grid[i][j] + min(dp[j], dp[j+1])
                else:
                    dp[j] = grid[i][j] + dp[j]
            # print(dp)
        return dp[0]
    def minPathSum2DDP(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [[float('inf')] * C for _ in range(R)]
        dp[0][0] = grid[0][0]
        for i in range(1, R):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, C):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[R-1][C-1]
    def minPathSumWithMemo(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[-1] * C for _ in range(R)]
        dp[R-1][C-1] = grid[R-1][C-1]
        def solve(r, c):
            if min(r, c)<0 or r==R or c==C:
                return float('inf')
                
            if dp[r][c]!=-1:
                return dp[r][c]
            
            curr = grid[r][c] + min(solve(r, c+1), solve(r+1, c))
            dp[r][c] = curr
            return curr
        return solve(0,0)
        

