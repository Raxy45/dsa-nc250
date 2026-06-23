class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(u_nums):
            if not u_nums: return 0
            if len(u_nums) == 1: return u_nums[0]

            dp = [0] * len(u_nums)
            dp[0] = u_nums[0]
            dp[1] = max(dp[0], u_nums[1])
            for i in range(2, len(u_nums)):
                dp[i] = max(u_nums[i]+dp[i-2], dp[i-1])
            return dp[-1]
        
        return max(helper(nums[0:len(nums)-1]), helper(nums[1:]))