class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(idx, remaining):
            print(idx, remaining)
            nonlocal ans, curr
            if remaining == 0:
                ans.append(curr.copy())
                return

            if remaining<0 or idx==len(candidates):
                return
            


            if candidates[idx] <= remaining:
                # @ take it
                curr.append(candidates[idx])
                while idx<(len(candidates)-1) and candidates[idx] == candidates[idx+1]:
                    idx += 1
                dfs(idx+1, remaining-candidates[idx])
                curr.pop()
            # skip it
            dfs(idx+1, remaining)
            
        curr = []
        dfs(0, target)
        return ans