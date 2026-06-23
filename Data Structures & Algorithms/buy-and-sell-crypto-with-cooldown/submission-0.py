class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # At any given point, 3 options:
        # 1. Buy
        # 2. Sell
        # 3. Skip
        n = len(prices)
        def solve(i, holding):
            print(i, holding)
            if i>=n:
                print('end reached')
                return 0
            
            if holding:
                # holding
                # either sell or skip
                return max(prices[i]+solve(i+2, False), solve(i+1, holding))
            
            # not holding
            # buy or skip
            return max(-prices[i]+solve(i+1, True), solve(i+1, False))
        return solve(0, False)
