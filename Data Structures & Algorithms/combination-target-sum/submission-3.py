class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subsets = []

        def solve(idx, total, subsets):
            if total == target:
                ans.append(subsets.copy())
                return
            
            if idx==len(nums) or total > target:
                return
            
            subsets.append(nums[idx])
            total += nums[idx]
            solve(idx, total, subsets)

            subsets.pop()
            total -= nums[idx]
            solve(idx+1, total, subsets)

        solve(0,0,subsets)
        return ans