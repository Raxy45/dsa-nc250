class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [None] * (n + 1)

        def solve(i):
            if i == n:
                return 0
            
            if dp[i] is not None:
                return dp[i]
            
            # Take 1
            res = stoneValue[i] - solve(i + 1)

            # Take 2
            if i + 1 < n:
                res = max(res,
                          stoneValue[i] + stoneValue[i+1] - solve(i + 2))

            # Take 3
            if i + 2 < n:
                res = max(res,
                          stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - solve(i + 3))

            dp[i] = res
            return res

        diff = solve(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"