class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*max(i-j, dp[i-j]))
        print(dp)
        return dp[n]
    def integerBreakTopDown(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        dp[2] = 1
        dp[1] = 1
        def solve(t):
            if t in dp:
                return dp[t]
            
            res = 1
            for i in range(1, t):
                curr_prod = i * max(t-i, solve(t-i))
                res = max(res, curr_prod)
            dp[t] = res
            return dp[t]
        return solve(n)