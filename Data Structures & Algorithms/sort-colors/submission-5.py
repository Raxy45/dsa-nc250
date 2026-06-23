class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, r = 0, 0, len(nums)-1
        for m in range(len(nums)):
            match nums[m]:
                case 0:
                    nums[l], nums[m] = nums[m], nums[l]
                    l += 1
                case 2:
                    nums[r], nums[m] = nums[m], nums[r]
                    