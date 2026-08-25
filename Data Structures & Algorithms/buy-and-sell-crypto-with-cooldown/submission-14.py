class Solution:
    def maxProfit(self, prices):
        dp = [[0, 0] for _ in range(len(prices) + 2)]

        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                if j==1:
                    # print('True for holding', i, j)
                    dp[i][j] = max(prices[i] + dp[i+2][0], dp[i+1][1])
                else:
                    # print('not holding', i, j)
                    dp[i][j] = max(-prices[i] + dp[i+1][1], dp[i+1][0])
            # print(dp)
        return dp[0][0]


    def maxProfitTopDown(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx, holding):
            if (idx, holding) in dp:
                return dp[(idx, holding)]
            if idx>=len(prices):
                return 0
            
            curr = 0
            if holding:
                curr = max(prices[idx] + dfs(idx+2, False), \
                           dfs(idx+1, True))    # NOT SELL
            else:
                curr = max(-prices[idx] + dfs(idx+1, True), 
                           dfs(idx+1, False)) # Not Buy
            dp[(idx, holding)] = curr
            return dp[(idx, holding)]
        return dfs(0, False)