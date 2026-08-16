class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_idx = 0

        for i in range(len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
            ans = max(ans, prices[i] - prices[min_idx])
        return ans
        