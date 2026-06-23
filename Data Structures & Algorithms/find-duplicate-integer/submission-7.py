class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number = nums[i]
            idx = abs(number)-1
            if nums[idx]<0: return abs(number)
            nums[idx] = -nums[idx]