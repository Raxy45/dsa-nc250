class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, middle, end = 0, 0, len(nums) - 1
        while middle <= end:
            match nums[middle]:
                case 0:
                    nums[start], nums[middle] = nums[middle], nums[start]
                    start += 1
                    middle += 1
                case 1:
                    middle += 1
                case 2: 
                    nums[end], nums[middle] = nums[middle], nums[end]
                    end -= 1
            
        