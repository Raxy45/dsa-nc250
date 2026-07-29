class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx, holding):
            if idx >= len(prices):
                return 0
            
            if (idx, holding) in dp:
                return dp[(idx, holding)]
            
            if holding:
                # Selling
                curr_pf = prices[idx] + dfs(idx+2, False)
                curr_pf = max(curr_pf, dfs(idx+1, True))
            else:
                # Buying
                curr_pf = -prices[idx] + dfs(idx+1, True) 
                curr_pf = max(curr_pf, dfs(idx+1, False))
            
            dp[(idx, holding)] = curr_pf
            return curr_pf
        return dfs(0, False)