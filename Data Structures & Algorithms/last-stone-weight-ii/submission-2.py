class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum) // 2
        dp = {}

        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            
            if total>=target or i==len(stones):
                return abs(total - (stoneSum-total))
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
            return dp[(i, total)]
        return dfs(0, 0)