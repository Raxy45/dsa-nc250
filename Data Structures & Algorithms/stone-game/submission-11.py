class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(start, end):
            if start==end:
                return piles[end]
            if (start, end) in dp: return dp[(start, end)]
            
            curr = float('-inf')
            dp[(start, end)] = max(curr, piles[start] - dfs(start+1, end), \
                        piles[end] - dfs(start, end-1))
            return dp[(start, end)]
        
        return True if dfs(0, len(piles)-1) > 0 else False