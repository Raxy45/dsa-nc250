class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_subsets = []
        final_ans = []

        def solve(idx, curr_subsets):
            if idx ==len(nums):
                final_ans.append(curr_subsets.copy())
                return
            
            curr_subsets.append(nums[idx])
            solve(idx+1, curr_subsets)

            curr_subsets.pop()
            solve(idx+1, curr_subsets)
        solve(0, curr_subsets)
        return final_ans
