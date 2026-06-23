class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(0, len(prices)-1):
            current_profit = 0 
            for j in range(i+1, len(prices)):
                current_profit = prices[j] - prices[i]
                max_p = max(current_profit, max_p)
        return max_p