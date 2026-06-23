class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def solve(r, c):
            
            if dp[r][c] != -1:
                return dp[r][c]

            curr = 0
            for dr, dc in deltas:
                ur, uc = r+dr, c+dc
                if 0<=ur<m and 0<=uc<n and matrix[ur][uc] > matrix[r][c]:
                    curr = max(curr, solve(ur, uc))
            dp[r][c] = 1+curr
            return dp[r][c]
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, solve(i, j))
        return result
            