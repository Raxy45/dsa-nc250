class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        if len(nums)<1:
            return 1
        
        for j in range(1, len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1] = nums[j]
                i+=1
        return i+1
        i = j = 0
        while j < len(nums):
            while j<len(nums) and nums[i] == nums[j]:
                # print('inside i, j',i , j)
                j += 1
            if j<len(nums):
                # print('out i, j ', i, j)
                nums[i+1]=nums[j]
                i+=1
                j+=1
        return i+1
        
        i, k = 0, 1
        if len(nums) == 1:
            return 1
        while i+1<len(nums) and k < len(nums):
            while k<len(nums) and nums[i] == nums[k]:
                k += 1
            if k < len(nums):
                nums[i+1]=nums[k]
                i += 1
                k += 1
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
        