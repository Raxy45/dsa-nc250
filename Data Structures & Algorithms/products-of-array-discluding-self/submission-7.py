class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = [1] * len(nums)
        curr = 1
        for i in range(len(nums)):
            product_arr[i] = curr
            curr *= nums[i]
        
        curr = 1
        for j in range(len(nums)-1, -1, -1):
            product_arr[j] = curr * product_arr[j]
            curr *= nums[j]
        
        return product_arr