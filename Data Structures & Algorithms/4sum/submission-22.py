class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]: continue
                required_sum = target - nums[i] - nums[j]
                