class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {n:0}
        def solve(i):
            if i in dp:
                return dp[i]
            
            dp[i] = max(-1, stoneValue[i] - solve(i+1))

            if (i+1)<n:
                dp[i] = max(dp[i], (stoneValue[i]+stoneValue[i+1]) - solve(i+2))
            
            if (i+2) < n:
                dp[i] = max(dp[i], (stoneValue[i]+stoneValue[i+1] + stoneValue[i+2]) - solve(i+3))
            
            return dp[i]
        diff = solve(0)
        if diff==0:
            return "Tie"
        if diff>0:
            return "Alice"
        return "Bob"