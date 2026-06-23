class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[-1]*len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            ans += 1
            dp[i][i] = 1

        def check(i, j):
            if j<i: return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                dp[i][j] = check(i+1, j-1)
                return dp[i][j]
            
            dp[i][j] = 0
            return dp[i][j]

        print(dp)
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                print(i, j)
                if s[i] == s[j] and dp[i+1][j-1]==1:
                    print('hre')
                    dp[i][j] = 1
                    ans += 1
                if s[i] == s[j]:
                    if (j-1) < (i+1):
                        dp[i][j] = 1
                        ans += 1
                
        return ans