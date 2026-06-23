class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            abs_val = abs(nums[i])
            idx = abs_val - 1
            if nums[idx]<0:
                return abs(nums[i])
            nums[idx] = -nums[idx]