class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_p = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                temp = nums[z_p]
                nums[z_p] = nums[i]
                nums[i] = temp
                z_p += 1
        print(nums)
        