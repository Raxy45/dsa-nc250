class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[-1] * l2 for _ in range(l1)]
        def solve(i, j):
            if i==l1 or j==l2:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + solve(i+1, j+1)
                return dp[i][j]

            dp[i][j] = max(solve(i+1, j), solve(i, j+1))
            return dp[i][j]
        return solve(0, 0)