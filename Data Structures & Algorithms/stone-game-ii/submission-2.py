class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = [0] * len(piles)
        curr = 0
        for i in range(len(piles)-1, -1, -1):
            suffix_sum[i] = curr+piles[i]
            curr = suffix_sum[i]
        
        dp = {}
        def dfs(idx, m):
            if (idx, m) in dp: return dp[(idx, m)]
            if idx>=len(piles): return 0

            max_delta = float('-inf')
            curr = 0
            for i in range(1, (2*m)+1):
                if (i+idx-1)>=len(piles):
                    break
                max_delta = max(max_delta, suffix_sum[idx+i-1]-dfs(idx+i, max(m, i)))
            dp[(idx, m)] = max_delta
            return dp[(idx, m)]
        return dfs(0, 1)