class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_mx, c_min = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            temp_min = min(nums[i], nums[i]*c_min, nums[i]*c_mx)
            temp_mx = max(nums[i], nums[i]*c_mx, nums[i] * c_min)

            c_mx, c_min = temp_mx, temp_min
            ans = max(ans, c_mx)
        print(nums)
        return ans