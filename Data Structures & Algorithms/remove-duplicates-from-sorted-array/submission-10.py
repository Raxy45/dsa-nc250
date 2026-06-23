class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                nums[k+1] = nums[i]
                k += 1
        return k+1