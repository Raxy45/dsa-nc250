class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(c_sum, i):
            if c_sum == target:
                ans.append(subset.copy())
                return
            
            if c_sum > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(c_sum+candidates[i], i+1)

            subset.pop()
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(c_sum, i+1)
        
        ans, subset = [], []
        dfs(0,0)
        return ans
