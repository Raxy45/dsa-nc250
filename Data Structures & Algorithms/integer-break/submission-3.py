class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def solve(t):
            if t in dp: return dp[t]

            curr_mx_product = -1
            for i in range(1, t):
                curr = i * max(t-i, solve(t-i))
                curr_mx_product = max(curr_mx_product, curr)
            dp[t] = curr_mx_product
            return curr_mx_product
        return solve(n)