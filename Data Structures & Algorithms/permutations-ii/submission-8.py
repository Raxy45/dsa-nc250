class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(nums, idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[idx]:
                    continue
                nums[i], nums[idx] = nums[idx], nums[i]
                
                solve(nums, idx+1)

                nums[idx], nums[i] = nums[i], nums[idx]
        nums.sort()
        solve(nums, 0)
        return res