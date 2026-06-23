class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 1
        if len(nums) == 1:
            return 1
        
        while i+1<len(nums)-1 and k < len(nums):
            while k < len(nums) and nums[i] == nums[k]:
                k += 1
            if k < len(nums):
                nums[i+1], nums[k] = nums[k], nums[i+1]
                i += 1
                k+= 1
        return i+1






        i, p = 1, 0
        if len(nums) == 1:
            return 1

        while i < len(nums):
            # print(nums, i, p)
            while nums[p] == nums[i]:
                i+=1
                # print(i)
                if i>=len(nums):
                    return p+1
            nums[p+1]=nums[i]
            p+=1
            i+=1

        # while i<len(nums):
        #     if nums[p]!=nums[i]:
        #         nums[p+1] = nums[i]
        #         i += 1
        #         p += 1
        #     else:
        #         i+= 1
        return p+1
        