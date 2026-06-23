class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        nums.sort()
        def solve(idx):
            if idx==len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[idx])
            solve(idx+1)

            subset.pop()
            while (idx+1)<len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            
            solve(idx+1)
        
        solve(0)
        return ans