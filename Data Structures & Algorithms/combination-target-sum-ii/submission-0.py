class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        ans = []
        candidates.sort()
        def solve(idx, total):
            print(subset, idx, total)
            if total == target:
                if subset.copy() not in ans:
                    ans.append(subset.copy())
                return
            
            if idx == len(candidates) or total > target:
                return
            
            subset.append(candidates[idx])
            solve(idx+1, total+candidates[idx])

            subset.pop()
            solve(idx+1, total)
        
        solve(0, 0)
        return ans