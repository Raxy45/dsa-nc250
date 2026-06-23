class Solution:
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