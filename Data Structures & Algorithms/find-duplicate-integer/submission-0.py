class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            curr_index = nums[i]-1
            if nums[curr_index]==0:
                return nums[i]
            nums[curr_index] = 0