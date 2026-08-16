class Solution:
    def change(self, amount, coins):
        dp = [[0] * len(coins) for _ in range(amount+1)]
        for i in range(len(coins)):
            dp[0][i] = 1
        # print(
        #     dp
        # )
        for req_amt in range(1, amount+1):
            # print('here')
            for i in range(len(coins)-1, -1, -1):
                # print(coins[i], req_amt)
                if coins[i] > req_amt:
                    # print(coins[i], req_amt)
                    continue
                dp[req_amt][i] = dp[req_amt - coins[i]][i]
                
                if (i+1) < len(coins):
                    dp[req_amt][i] += dp[req_amt][i+1]
        # print(dp)
        return dp[amount][0]
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