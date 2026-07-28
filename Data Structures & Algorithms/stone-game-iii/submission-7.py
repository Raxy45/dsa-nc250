class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {n: 0}

        def dfs(i):
            if i in dp: return dp[i]

            res = stoneValue[i] - dfs(i+1)

            if (i+1) < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] - dfs(i+2))

            if (i+2) < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dfs(i+3))
            
            return res

        
        diff = dfs(0)
        if diff>0: return 'Alice'
        elif diff == 0: return 'Tie'
        return 'Bob'