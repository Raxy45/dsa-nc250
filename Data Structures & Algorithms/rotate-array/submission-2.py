class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums,l,r):
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1 
                r -=1
        
        while k > 0:
            reverse(nums, 0, len(nums)-1)
            reverse(nums, 1, len(nums)-1)
            k -=1
    def rotateBasic(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            i = len(nums)-2
            temp = nums[len(nums)-1]
            # print('i initially: ', i)
            # print('k initially: ', k)
            # print('temp: ', temp)
            # print('nums: ', nums)
            while i>=0:
                # print(i, nums[i])
                nums[i+1]=nums[i]
                i -= 1
                # print('nums intermediate: ', nums)
            nums[i+1] = temp
            k -= 1
            # print('i post: ', i)
            # print('k post: ', k)
            # print('temp: ', temp)
            # print('nums: post', nums)
            # print('*'*10)
        