class Solution:
    def climbStairs(self, n):
        p2, p1 = 1, 2
        for i in range(2, n):
            curr = p1+p2
            temp = p1
            p1 = curr
            p2 = temp
        return p1
    def climbStairsBottomUp(self, n):
        if n==1: return 1
        if n==2: return 2
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    def climbStairsRecMemo(self, n: int) -> int:
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