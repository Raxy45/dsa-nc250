class Solution:
    def integerBreak(self, n: int) -> int:
        dp = defaultdict()
        dp[1] = 1
        def solve(t):
            # print(t, dp)
            if t in dp:
                return dp[t]

            res = -1
            for i in range(1, t):
                # print('i, t-i', i, t-i)
                curr_prod = i * solve(t-i)
                # print('For T',t, 'curr_prod:', curr_prod, i, t-i)
                res = max(res, curr_prod, i*(t-i))
            dp[t] = res
            return dp[t]
        return solve(n)