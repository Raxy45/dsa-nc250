class Solution:
    def numSquares(self, n: int) -> int:
        ip = []
        for i in range(1, n+1):
            if i**2 <=n:
                ip.append(i**2)
        
        dp = defaultdict()
        dp[0] = 0
        print(ip)
        def solve(t):
            if t in dp:
                return dp[t]
            
            res = float('inf')
            for n in ip:
                if n<=t:
                    res = min(res, 1+solve(t-n))
            dp[t] = res
            return dp[t]
        return solve(n)