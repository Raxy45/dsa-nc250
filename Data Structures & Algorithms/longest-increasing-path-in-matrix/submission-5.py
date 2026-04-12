class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
class SolutionRecMemo:
    def longestIncreasingPathRecMemo(self, matrix: List[List[int]]) -> int:
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
            