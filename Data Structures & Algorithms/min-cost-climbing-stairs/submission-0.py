class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = 0
        i = len(cost)
        while i>-1:
            if cost[i-2]<=cost[i-1]:
                ans += cost[i-2]
                i = i - 2
            else:
                ans += cost[i-1]
                i = i - 1
            if i == 0 or i == 1:
                break
        return ans