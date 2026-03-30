class Solution:
    def numSquares(self, n: int) -> int:
        ip = []
        for i in range(1, int(n**0.5)+1):
            ip.append(i*i)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for t in range(1, n+1):
            for i in ip:
                if t>=i:
                    dp[t] = min(dp[t], 1+dp[t-i])
        return dp[n]
    def numSquaresTopDown(self, n: int) -> int:
        ip = []
        for i in range(1, int(n**0.5)+1):
            ip.append(i*i)
        dp = defaultdict(int)
        dp[0] = 0
        def solve(t):
            if t in dp:
                return dp[t]
            
            min_count = float('inf')
            for i in ip:
                if t>=i:
                    min_count = min(min_count, 1+solve(t-i))
            dp[t] = min_count
            return dp[t]
        return solve(n)