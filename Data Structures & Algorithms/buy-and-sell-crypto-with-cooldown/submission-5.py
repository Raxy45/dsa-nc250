class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        next_2 = [0, 0]
        next_1 = [0, 0]
        curr =   [0, 0]
        for i in range(n-1, -1, -1):
            # non holding
            curr[0] = max(-prices[i] + next_1[1], next_1[0])
            
            # holding
            curr[1] = max(prices[i] + next_2[0], next_1[1])

            next_2, next_1 = next_1.copy(), curr.copy()
        return curr[0]
    def maxProfit2DDP(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            # not holding
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i+1][0])

            # holding    
            dp[i][1] = max(prices[i]+dp[i+2][0], dp[i+1][1])
        return dp[0][0]

    def maxProfitRecMemo(self, prices: List[int]) -> int:
        # At any given point, 3 options:
        # 1. Buy
        # 2. Sell
        # 3. Skip
        n = len(prices)
        dp = {}
        def solve(i, holding):
            # print(i, holding)
            if (i, holding) in dp:
                # print('end reached')
                return dp[(i, holding)]

            if i>=n:
                return 0

            if holding:
                # holding
                # either sell or skip
                dp[(i, holding)] = max(prices[i]+solve(i+2, False), solve(i+1, holding))
                return dp[(i, holding)]

            # not holding
            # buy or skip
            dp[(i, holding)] = max(-prices[i]+solve(i+1, True), solve(i+1, holding))
            return dp[(i, holding)]
        return solve(0, False)
