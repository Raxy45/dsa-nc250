class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float('-inf')] * (n+1)
        dp[1] = dp[2] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(j * (i-j),
                            j * dp[i-j],
                            dp[i])
        return dp[n]
    def integerBreakTopDown(self, n: int) -> int:
        cache = {0:1}
        # cache[j] = m
        # This represents the maximum product you can get to get j

        i = 0
        def dfs(req_sum):
            if req_sum in cache: return cache[req_sum]
            if req_sum < 0: return 0
            # if i>10: return 0

            curr_mx = float('-inf')
            for i in range(1, n):
                curr_mx = max(i*(req_sum-i), i * dfs(req_sum - i), curr_mx)
            cache[req_sum] = curr_mx
            return cache[req_sum]
        return dfs(n)

        