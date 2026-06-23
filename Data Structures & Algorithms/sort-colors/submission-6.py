class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m,r=0,0,len(nums)-1
        while m<r:
            match nums[m]:
                case 0:
                    nums[l], nums[m] = nums[m], nums[l]
                    l += 1
                    m += 1
                case 1:
                    m += 1
                case 2:
                    nums[r], nums[m] = nums[m], nums[r]
                    r -=1