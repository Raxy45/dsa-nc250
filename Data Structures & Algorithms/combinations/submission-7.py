class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            if len(subset) == k:
                ans.append(subset.copy())
                return 
            
            for j in range(i, n+1):
                subset.append(j)
                dfs(j+1)
                subset.pop()
        
        ans, subset = [], []
        dfs(1)
        return ans