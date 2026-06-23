class Solution:
    def numSquares(self, n: int) -> int:
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