class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contains_1 = False
        for i in range(len(nums)):
            if nums[i]==1:
                contains_1 = True
                
            elif nums[i] <= 0 or nums[i]>=len(nums):
                nums[i] = 1
        
        print(nums)
        if not contains_1: return 1

        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx-1] > 0:
                nums[idx - 1] = -nums[idx-1]
        print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)

















        contains_1 = False
        for i in range(len(nums)):
            if nums[i] == 1: 
                contains_1 = True
            if nums[i] <= 0 or nums[i]>len(nums):
                nums[i] = 1
        
        if not contains_1: return 1

        print(nums)
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0: return i+1
        
        return len(nums)+1