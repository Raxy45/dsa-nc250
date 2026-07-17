class Solution:
    def numSquares(self, n: int) -> int:
        in_arr = []
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            in_arr.append(i*i)
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        # indicates the minimum number of perfect squares required to get j
        for curr_sum in range(1, len(dp)):
            for i in in_arr:
                if curr_sum >= i:
                    dp[curr_sum] = min(dp[curr_sum], 1 + dp[curr_sum-i])
            # print('888888')
        return dp[n]
        

        