class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0 
        while i < (len(prices)-1):
            current_transaction = prices[i+1] - prices[i]
            if current_transaction > 0:
                profit += current_transaction
            i +=1
        return profit
