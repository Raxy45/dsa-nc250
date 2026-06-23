class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        def solve(prev, r, c):
            if min(r, c) < 0 or r==m or c==n or matrix[r][c]<=prev:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            # assume matrix[i] > prev -> always true
            right = solve(matrix[r][c], r, c+1)
            left  = solve(matrix[r][c], r, c-1)
            top   = solve(matrix[r][c], r-1, c)
            down  = solve(matrix[r][c], r+1, c)

            # print('from lhs, rhs', r,c, lhs, rhs)
            dp[r][c] = 1 + max(left, right, top, down)
            return dp[r][c]
        curr = 0
        for i in range(m):
            for j in range(n):
                curr = max(curr, solve(0, i, j))
        return curr
            