class Solution:
    def longestCommonSubsequence(self, t1, t2):
        l1, l2 = len(t1), len(t2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        ans = 0
        j_start = 0
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if t1[i]==t2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    continue
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

    def longestCommonSubsequenceRecWithMemo(self, text1: str, text2: str) -> int:
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