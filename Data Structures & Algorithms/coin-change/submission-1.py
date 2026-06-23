class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        def solve(t):
            print(t)
            if t in dp:
                return dp[t]
            
            min_coins = float('inf')
            for n in coins:
                if t>=n:
                    min_coins = min(min_coins, 1+solve(t-n))
            print('min coins for',t, 'is', min_coins)
            dp[t] = min_coins
            return dp[t]
        ans = solve(amount)
        return ans if ans!=float('inf') else -1