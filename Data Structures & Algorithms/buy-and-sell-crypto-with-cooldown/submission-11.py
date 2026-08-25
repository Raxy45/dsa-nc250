class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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