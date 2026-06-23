class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 1
        def solve(i):
            if i<0 or i>n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = solve(i-1) + solve(i-2)
            return dp[i]
        return solve(n)