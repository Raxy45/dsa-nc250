class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time Complexity: O(R * C)
            # - Each cell (r, c) is computed at most once due to memoization.
            # - After first computation, dp[r][c] is reused in O(1).

        # Space Complexity: O(R * C) + O(R + C)
            # - O(R * C) for dp table
            # - O(R + C) recursion stack (max path length from (0,0) to (R-1,C-1))
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * C for _ in range(R)]
        def solve(r, c):
            if min(r, c) < 0 or r==R or c==C or obstacleGrid[r][c] == 1:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = solve(r+1, c) + solve(r, c+1)
            return dp[r][c]
            
        dp[R-1][C-1] = 1 
        return solve(0, 0)
    
    def uniquePathsWithObstacles2DDP(self, obstacleGrid: List[List[int]]) -> int:
        # Time Complexity: O(R * C)
            # - We iterate over each cell of the grid exactly once.

        # Space Complexity: O(R * C)
            # - dp matrix stores number of ways for each cell.
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * C for _ in range(R)]
        for i in range(R):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1 
        
        for i in range(C):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        for i in range(1, R):
            for j in range(1, C):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[R-1][C-1]

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(M * N)
        # - We iterate over every cell in the grid exactly once.
        # Space Complexity: O(N)
        # - We use a 1D dp array of size N (number of columns).

        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]