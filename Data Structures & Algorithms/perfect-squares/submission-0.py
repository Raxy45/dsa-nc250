class Solution:
    def numSquares(self, n: int) -> int:
        ip = []
        for i in range(1, n+1):
            if i**2 <=n:
                ip.append(i**2)
        
        dp = defaultdict()
        dp[0] = 1
        print(ip)
        def solve(t, used):
            if t==0:
                return used
            
            for n in ip:
                if n<=t:
                    dp[t] = min(dp.get(t, float('inf')), solve(t-n, used+1))
            return dp.get(t, float('inf'))
        return solve(n, 0)