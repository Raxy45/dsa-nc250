class Solution:
    def longestCommonSubsequence(self, t1, t2):
        l1, l2 = len(t1), len(t2)
        dp = [[-1] * l2 for _ in range(l1)]
        ans = 0
        j_start = 0
        for i in range(l1):
            for j in range(j_start, l2):
                if t1[i]==t2[j]:
                    ans += 1
                    j_start += 1
        return ans
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