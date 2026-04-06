class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
            dp[(i, holding)] = max(-prices[i]+solve(i+1, True), solve(i+1, False))
            return dp[(i, holding)]
        return solve(0, False)
