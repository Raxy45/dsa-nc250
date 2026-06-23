class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            ans += 1
            dp[i][i] = True
        
        for L in range(2, n+1):
            for i in range(0, n+1 - L):
                j = i+L-1
                print(s[i], s[j])
                if s[i] == s[j] and L==2:
                    dp[i][j] = True
                    ans += 1
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        return ans