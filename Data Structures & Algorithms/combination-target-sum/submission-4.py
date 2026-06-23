class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subsets = []

        def solve(idx, total):
            if total == target:
                ans.append(subsets.copy())
                return
            
            if idx==len(nums) or total > target:
                return
            
            subsets.append(nums[idx])
            total += nums[idx]
            solve(idx, total)

            subsets.pop()
            total -= nums[idx]
            solve(idx+1, total)

        solve(0,0)
        return ans