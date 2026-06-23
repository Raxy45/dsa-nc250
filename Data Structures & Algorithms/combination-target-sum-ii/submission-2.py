class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, subset = [], []

        candidates.sort()
        def solve(idx, total, subset):
            if total == target:
                ans.append(subset.copy())
                return
            
            if total > target or idx == len(candidates):
                return

            # if idx>1 and candidates[idx] == candidates[idx-1]:
            #     return
            for i in range(idx, len(candidates)):
                
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                total += candidates[i]
                
                solve(i+1, total, subset)

                subset.pop()
                total -= candidates[i]

        solve(0, 0, [])
        return ans