class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_subsets = []
        curr_subset = []

        def solve(idx):
            print('subset', curr_subset, 'idx', idx)
            if sum(curr_subset) >= target or idx==len(nums):
                if sum(curr_subset) == target:
                    ans_subsets.append(curr_subset.copy())
                print('in here',idx)
                return
            

            if sum(curr_subset) < target:
                curr_subset.append(nums[idx])
                solve(idx)
                curr_subset.pop()

            solve(idx+1)

        solve(0)
        return ans_subsets
            
            