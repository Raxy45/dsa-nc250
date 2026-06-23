class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        low = 0
        high = 1
        if len(prices) == 1:
            return 0
        for i in range(0, len(prices)):
            print(prices[i])
            print('current low: ', prices[low])
            print('current high: ', prices[high])
            if prices[i] < prices[low]:
                print('updating low: ')
                print('low old , low new ', prices[low], prices[i])
                low = i
            if i!=0 and i>low and prices[i] >= prices[high]:
                print('updating high: ')
                print('high old , high new ', prices[high], prices[i])
                high = i
                print('current profit: ', price[high]-prices[low])
                max_p = max(max_p, prices[high]-prices[low])
        return max_p
        
        # max_p = 0
        # for i in range(0, len(prices)-1):
        #     current_profit = 0 
        #     for j in range(i+1, len(prices)):
        #         current_profit = prices[j] - prices[i]
        #         max_p = max(current_profit, max_p)
        # return max_p