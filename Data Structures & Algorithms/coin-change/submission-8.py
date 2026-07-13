class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        cache = {0:0}
        def dfs(remaining):
            if remaining in cache: return cache[remaining]
            if remaining == 0: return 0
            if remaining < 0: return float('inf')

            min_coins = float('inf')
            for i in range(len(coins)):
                curr_req_coins = 1 + dfs(remaining - coins[i])
                if curr_req_coins != float('inf'):
                    min_coins = min(min_coins, curr_req_coins)
            cache[remaining] = min_coins
            return cache[remaining]
        dfs(amount)
        # print(cache)
        return cache[amount] if cache[amount] != float('inf') else -1
        