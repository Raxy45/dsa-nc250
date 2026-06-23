class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])
        

class SolutionWithMemo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def solve(i):
            if i>=len(cost):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(solve(i+1), solve(i+2))
            return cache[i]
        return min(solve(0), solve(1))

class SolutionWithoutMemo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def solve(i):
            if i>=len(cost):
                return 0
            
            return cost[i] + min(solve(i+1), solve(i+2))
        return min(solve(0), solve(1))