class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, p = 1, 0
        if len(nums) == 1:
            return 1
        while i<len(nums):
            if nums[p]!=nums[i]:
                nums[p+1] = nums[i]
                i += 1
                p += 1
            else:
                i+= 1
        return p+1
        