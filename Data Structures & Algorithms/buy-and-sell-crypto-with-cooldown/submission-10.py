class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(idx, holding):
            if idx>=len(prices):
                return 0
            
            curr = 0
            if holding:
                curr = max(prices[idx] + dfs(idx+2, False), \
                           dfs(idx+1, True))    # NOT SELL
            else:
                curr = max(-prices[idx] + dfs(idx+1, True), 
                           dfs(idx+1, False)) # Not Buy
            return curr
        return dfs(0, False)