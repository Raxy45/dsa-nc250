class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx, holding):
            if idx >= len(prices):
                return 0
            
            if (idx, holding) in dp:
                return dp[(idx, holding)]
            
            if holding:
                sell = prices[idx] + dfs(idx + 2, False)
                skip = dfs(idx + 1, True)
                curr_pf = max(sell, skip)
            else:
                buy = -prices[idx] + dfs(idx + 1, True)
                skip = dfs(idx + 1, False)
                curr_pf = max(buy, skip)
            
            dp[(idx, holding)] = curr_pf
            return curr_pf
        return dfs(0, False)