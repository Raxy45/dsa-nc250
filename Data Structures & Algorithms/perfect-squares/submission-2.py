class SolutionTopDown:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5) + 1)]
        dp = {0: 0}

        def solve(t):
            if t in dp:
                return dp[t]

            res = float('inf')
            for sq in squares:
                if sq <= t:
                    res = min(res, 1 + solve(t - sq))

            dp[t] = res
            return res

        return solve(n)

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]