class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        ans = []
        candidates.sort()
        def solve(idx, total):
            if total == target:
                ans.append(subset.copy())
                return
            
            if idx == len(candidates) or total > target:
                return
            
            curr = candidates[idx]
            subset.append(candidates[idx])
            
            solve(idx+1, total+curr)
            subset.pop()

            while (idx+1)<len(candidates) and candidates[idx+1] == candidates[idx]:
                idx += 1
            
            solve(idx+1, total)
        
        solve(0, 0)
        return ans