class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1, p2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(p1, p2)
            p1 = p2
            p2 = curr
        return min(p2, p1)
    def minCostClimbingStairsRec(self, cost: List[int]) -> int:
        cache = {}
        def dfs(step):
            if step >= len(cost): return 0
            if step in cache: return cache[step]
            cache[step] = cost[step] + min(dfs(step+1), dfs(step+2))
            return cache[step]
        return min(dfs(0), dfs(1))
        