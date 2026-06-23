class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, max_p = float('inf'), 0
        for i in prices:
            max_p = max(max_p, i - current_min)
            current_min = min(current_min, i)
        return max_p