class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)
        def solve(i):
            if i==len(s):
                return 1
            if int(s[i]) == 0: return 0
            if i in dp:
                return dp[i]
            dp[i] += solve(i+1)

            if (i+1) < len(s):
                if int(s[i:i+2]) < 27:
                    dp[i]+= solve(i+2)
            return dp[i]
        solve(0)
        return dp[0]
