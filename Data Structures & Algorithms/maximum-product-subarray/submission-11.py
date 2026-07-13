class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_arr = [float('-inf')] * len(nums)
        min_arr = [float('inf')] * len(nums)
        ans = float('-inf')
        mx_arr[0] = min_arr[0] = nums[0]
        for i in range(1, len(nums)):
            mx_arr[i] = max(nums[i], nums[i] * mx_arr[i-1])
            min_arr[i] = min(nums[i], nums[i] * min_arr[i-1])
            ans = max(ans, mx_arr[i], nums[i]*min_arr[i-1])


        return ans
        