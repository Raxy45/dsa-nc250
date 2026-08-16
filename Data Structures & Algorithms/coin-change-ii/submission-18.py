class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)-1, -1, -1):
            for req in range(coins[i], amount+1):
                prev = dp[req]
                dp[req] = dp[req - coins[i]] # take current coin
                
                if (i+1) < len(coins):
                    dp[req] += prev # skip current coin
        return dp[amount]
    def change2dDP(self, amount, coins):
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for i in range(len(coins)-1, -1, -1):
            for req in range(1, amount+1):
                if coins[i] <= req:
                    dp[i][req] = dp[i][req - coins[i]] # take current coin
                
                if (i+1) < len(coins):
                    dp[i][req] += dp[i+1][req] # skip current coin
        return dp[0][amount]
        
    def changeRec(self, amount: int, coins: List[int]) -> int:
        ans = 0
        n = len(coins)
        dp = {}
        def dfs(idx, remaining):
            if (idx, remaining) in dp:
                return dp[(idx, remaining)]
            if remaining == 0:
                return 1
            if idx == n:
                return 0
            
            curr = 0
            for i in range(idx, n):
                if coins[i]>remaining:
                    continue
                curr += dfs(i, remaining-coins[i])
            dp[(idx, remaining)] = curr
            return dp[(idx, remaining)]
        return dfs(0, amount)

        # TC is:
        # n * a -> states from idx 0 to len(coins) are changing -> n and the amount is also changing from a to 0 -> a
        # SC is:
        # a * n