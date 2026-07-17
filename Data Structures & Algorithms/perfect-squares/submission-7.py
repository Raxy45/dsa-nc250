class Solution:
    def numSquares(self, n: int) -> int:
        in_arr = []
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            in_arr.append(i*i)
        
        dp = [0] * (n+1)
        dp[0] = 1
        # print(in_arr, dp)
        for curr_sum in range(1, len(dp)):
            curr_least = float('inf')
            for i in in_arr:
                if curr_sum >= i:
                    if (curr_sum - i) == 0:
                        curr_least = 1
                        break
                    if (dp[curr_sum - i]) > 0:
                        dp[curr_sum] = 1 + dp[curr_sum - i]
                if dp[curr_sum] != 0:
                    curr_least = min(dp[curr_sum], curr_least)
            
            if curr_least != float('inf'):
                dp[curr_sum] = curr_least
            # print('888888')
        return dp[n]
        

        