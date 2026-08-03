class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        R, C = len(matrix), len(matrix[0])
        def dfs(r, c):
            curr = 0
            if (r, c) in dp: return dp[(r, c)]

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ur, uc = r + dr, c + dc
                if min(ur, uc) < 0 or ur==R or uc==C: 
                    continue
                
                if matrix[ur][uc] > matrix[r][c]:
                    curr = max(curr, dfs(ur, uc))
            dp[(r, c)] = 1 + curr
            return dp[(r, c)]
        
        max_len = 1
        for i in range(R):
            for j in range(C):
                max_len = max(max_len, dfs(i, j))
        return max_len
        