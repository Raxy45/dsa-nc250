class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(total, i):
            if total == target:
                ans.append(subset.copy())
                return
            
            if total > target: return

            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]: continue
                subset.append(candidates[j])
                dfs(total+candidates[j], j+1)
                subset.pop()
        
        subset, ans = [], []
        candidates.sort()
        dfs(0, 0)
        return ans