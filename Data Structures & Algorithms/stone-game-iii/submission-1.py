class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            # Take 1 stone
            dp[i] = stoneValue[i] - solve(i + 1)
            
            # Take 2 stones
            if i + 1 < n:
                dp[i] = max(dp[i],
                            stoneValue[i] + stoneValue[i+1] - solve(i + 2))
            
            # Take 3 stones
            if i + 2 < n:
                dp[i] = max(dp[i],
                            stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - solve(i + 3))
            
            return dp[i]

        diff = solve(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"


        # Time Complexity: O(n)
        # - Each index i is computed once
        # - At each i, we do constant work (3 choices)

        # Space Complexity: O(n)
        # - dp array of size n
        # - recursion stack up to O(n)