class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for a in range(1, len(dp)):
            for n in coins:
                if a>=n:
                    dp[a] = min(dp[a], 1+dp[a-n])
        return dp[amount] if dp[amount] != float('inf') else -1
    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        def solve(t):
            if t in dp:
                return dp[t]
            
            min_coins = float('inf')
            for n in coins:
                if t>=n:
                    min_coins = min(min_coins, 1+solve(t-n))
            dp[t] = min_coins
            return dp[t]
        ans = solve(amount)
        return ans if ans!=float('inf') else -1