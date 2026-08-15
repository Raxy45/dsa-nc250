class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {}
        def dfs(idx, remaining, curr_list):
            print(idx, remaining, curr_list)
            if remaining == 0:
                return curr_list
            if (idx, remaining) in dp:
                return dp[(idx, remaining)]
            if idx >=len(candidates):
                return []
            
            curr_ans = []
            for i in range(idx, len(candidates)):
                if candidates[i] > remaining:
                    continue
                curr_list.append(candidates)

                new_lists = dfs(i + 1, remaining - candidates[i], curr_list)
                if len(new_lists) > 0:
                    curr_ans.append(new_lists)
                curr_list.pop()

            dp[(idx, remaining)] = curr_ans.copy()
            print('For idx, remaining', (idx, remaining), 'ans is ', curr_ans)
            return dp[(idx, remaining)]
        ans = dfs(0, target, [])
        print(dp[(0, target)])