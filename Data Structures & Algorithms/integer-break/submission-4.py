class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1  # base

        for t in range(n+1):
            curr_mx_product = 0
            for i in range(t):
                prod = i * max(t-i, dp[t-i])
                curr_mx_product = max(curr_mx_product, prod)
            dp[t] = curr_mx_product
        return dp[n]

    def integerBreakTopDwn(self, n: int) -> int:
        # Time Complexity: O(n^2)
            # - There are n states (t = 1 to n)
            # - For each state, we try all splits i from 1 to t-1 → O(n)
        # - Total = O(n * n) = O(n^2)

        # Space Complexity: O(n)
            # - dp stores results for n states
            # - recursion stack depth up to O(n)
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