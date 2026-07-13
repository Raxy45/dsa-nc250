class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans_arr = [float('-inf')] * len(nums)
        for i in range(len(nums)):
            ans_arr[i] = max(ans_arr[i], nums[i])
            if i > 0:
                ans_arr[i] = max(ans_arr[i], nums[i] * ans_arr[i-1])
        return max(ans_arr)
        