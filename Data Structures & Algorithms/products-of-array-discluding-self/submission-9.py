class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        curr = nums[0]
        for i in range(1, len(nums)):
            temp[i] = curr
            curr = curr * nums[i]
        print(temp)

        curr = 1
        # print('hhh')
        for i in range(len(nums)-1, -1, -1):
            # print('.h?')
            # print(i, curr, temp[i], nums[i])
            temp[i] = curr * temp[i]
            curr = curr * nums[i]
        # print(temp)
        return temp








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