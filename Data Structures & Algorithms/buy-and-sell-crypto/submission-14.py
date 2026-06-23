class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        low = 0
        for i in range(1,len(prices)):
            max_p = max(max_p, prices[i]-prices[low])
            if prices[i]<prices[low]:
                low = i
        return max_p
        max_p = 0
        low,j=0,0
        if len(prices)==1:
            return 0

        for j in range(1, len(prices)):
            if prices[j]<prices[low]:
                low = j
            max_p = max(max_p, prices[j]-prices[low])

        return max_p