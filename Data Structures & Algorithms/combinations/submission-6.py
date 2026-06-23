class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            if len(subset) == k:
                ans.append(subset.copy())
                return
            
            if i>n: return
            subset.append(i)
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        ans, subset = [], []
        dfs(1)
        return ans