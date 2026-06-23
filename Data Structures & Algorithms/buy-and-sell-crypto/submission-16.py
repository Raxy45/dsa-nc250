class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, max_p = float('inf'), float('-inf')
        for price in prices:
            current_min = min(current_min, price)
            max_p = max(max_p, price-current_min)
        return max_p