class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp, ans = [[-1] * n for _ in range(n)], 0
        def checkPali(l, r):
            if r<l: return 1
            if dp[l][r] != -1:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = checkPali(l+1, r-1)
                return dp[l][r]
            
            dp[l][r] = 0
            return dp[l][r]
        for i in range(n):
            for j in range(i, n):
                if checkPali(i, j)==1:
                    ans += 1
        # print(dp)
        return ans