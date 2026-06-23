class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_subsets = []
        curr_subset = []

        def solve(idx, total):
            if total >= target or idx==len(nums):
                if total == target:
                    ans_subsets.append(curr_subset.copy())
                return
            

            if sum(curr_subset) < target:
                total += nums[idx]
                curr_subset.append(nums[idx])
                solve(idx, total)
                total -= nums[idx]
                curr_subset.pop()

            solve(idx+1, total)

        solve(0, 0)
        return ans_subsets
            
            