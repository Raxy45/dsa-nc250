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
        
        o_p = z_p
        for i in range(z_p, len(nums)):
            if nums[i] == 1:
                temp = nums[o_p]
                nums[o_p] = nums[i]
                nums[i] = temp
                o_p += 1
        print(nums)

        