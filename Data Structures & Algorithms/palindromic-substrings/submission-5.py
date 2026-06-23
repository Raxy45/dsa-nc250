class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s))]
        ans = 0
        def check(i, j):
            if j<i: return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                dp[i][j] = check(i+1, j-1)
                return dp[i][j]
            
            dp[i][j] = 0
            return dp[i][j]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j)==1:
                    ans += 1

        return ans