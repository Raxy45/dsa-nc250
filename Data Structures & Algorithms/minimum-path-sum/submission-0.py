class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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
        

