class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx, holding):
            # print(idx, holding, dp)
            # print('***')
            if idx >= len(prices):
                return 0
            
            if (idx, holding) in dp:
                return dp[(idx, holding)]
            
            if holding!=-1:
                # Selling
                curr_pf = prices[idx] - holding + dfs(idx+2, -1)
                curr_pf = max(curr_pf, dfs(idx+1, holding))
            elif holding == -1:
                # Buying
                curr_pf = max(dfs(idx+1, prices[idx]), dfs(idx+1, -1))
            
            # print(curr_pf, 'is for', idx, holding)
            dp[(idx, holding)] = curr_pf
            return curr_pf
        return dfs(0, -1)