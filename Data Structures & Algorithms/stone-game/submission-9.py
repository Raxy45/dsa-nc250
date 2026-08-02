class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(start, end):
            if start==end:
                return piles[end]
            
            curr = float('-inf')
            curr = max(curr, piles[start] - dfs(start+1, end), \
                        piles[end] - dfs(start, end-1))
            return curr
        
        return True if dfs(0, len(piles)-1) > 0 else False

            
        