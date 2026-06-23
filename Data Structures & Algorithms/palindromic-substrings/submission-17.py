class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp, ans = [[False] * n for _ in range(n)], 0
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i+l - 1
                if l == 1:
                    dp[i][j] = True
                elif l==2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                
                if dp[i][j]:
                    ans += 1
                    
                
        # print(dp)
        return ans