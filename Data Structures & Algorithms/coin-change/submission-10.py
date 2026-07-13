class Solution:
    def coinChange(self, coins, amount):
        coin_change = [float('inf')] * (amount+1)
        coin_change[0] = 0
        for i in range(1, len(coin_change)):
            for j in range(len(coins)):
                # print('Target', i,  'Coin', coins[j])
                if i==coins[j]:
                    coin_change[i] = 1
                    # print('setting coin change to 1 for coin val', i, coins[j])
                    break
                if coins[j] > i:
                    # print('coin value', coins[j], 'is gt than', i)
                    continue
                coin_change[i] = min(coin_change[i], 1 + coin_change[i - coins[j]])
                # print('For coin and current value', coins[j], i, coin_change[i])
                # print(coin_change)
        # print(coin_change)
        return coin_change[amount] if coin_change[amount] != float('inf') else -1
    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
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
        return cache[amount] if cache[amount] != float('inf') else -1
        