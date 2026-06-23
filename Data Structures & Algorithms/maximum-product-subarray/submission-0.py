class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_mx, c_min = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            c_min = min(nums[i], nums[i]*nums[i-1])
            c_mx = max(nums[i], nums[i]*nums[i-1])
            nums[i] = max(c_mx, c_min)
            ans = max(ans, nums[i])
        print(nums)
        return ans