class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        low = 0
        if len(prices) == 1:
            return 0
        for i in range(1, len(prices)):
            print(prices[i])
            print('current low: ', prices[low])
            if prices[i] < prices[low]:
                print('updating low: ')
                print('low old , low new ', prices[low], prices[i])
                low = i
            else:
                print('current profit: ', prices[i]-prices[low])
                max_p = max(max_p, prices[i]-prices[low])
        return max_p
        
        # max_p = 0
        # for i in range(0, len(prices)-1):
        #     current_profit = 0 
        #     for j in range(i+1, len(prices)):
        #         current_profit = prices[j] - prices[i]
        #         max_p = max(current_profit, max_p)
        # return max_p