class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            nonlocal ans
            print(i, subset)
            if len(subset)==k:
                ans.append(subset.copy())
                return
            
            if i==n+1:
                return
            subset.append(i)
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        ans, subset = [], []
        dfs(1)
        return ans


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