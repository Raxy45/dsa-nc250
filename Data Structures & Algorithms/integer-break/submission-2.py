class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        def solve(t):
            if t in dp:
                return dp[t]

            res = float('-inf')
            for i in range(1, t):
                res = max(res, i * max(t - i, solve(t - i)))

            dp[t] = res
            return res

        return solve(n)