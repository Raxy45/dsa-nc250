class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_mx, c_mn = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]

            temp_mx = max(n, n*c_mx, n*c_mn)
            temp_mn = min(n, n*c_mx, n*c_mn)

            c_mx, c_mn = temp_mx, temp_mn
            ans = max(ans, c_mx)
        return ans