class Solution:
    def minCostClimbingStairs(self, cost):
        dp = {len(cost):0}
        def solve(i):
            if i>len(cost) or i<0:
                return 0
            if i in dp:
                return dp[i]
            curr_cost = cost[i] + min(solve(i+1), solve(i+2))
            dp[i] = curr_cost
            print(dp)
            return dp[i]
        print(dp)
        return min(solve(0), solve(1))
    def minCostClimbingStairsBottomUP(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])