class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_mx, c_min = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i]*c_mx, nums[i]*c_min)
            c_min = min(nums[i], nums[i]*c_min)
            c_mx = max(nums[i], nums[i]*c_mx)
            print(nums[i], c_min, c_mx)
            nums[i] = temp
            ans = max(ans, nums[i])
        print(nums)
        return ans