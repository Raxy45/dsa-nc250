class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin_idx, cmin = 0, float('inf')
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[cmin_idx]:
                cmin_idx = i
                continue
            ans = max(ans, prices[i] - prices[cmin_idx])
        return ans