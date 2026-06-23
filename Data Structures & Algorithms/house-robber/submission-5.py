class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    def robTopDownMemo(self, nums: List[int]) -> int:
        dp = {len(nums):0}
        def solve(i):
            if i in dp:
                return dp[i]
            if i>len(nums):
                return 0

            curr = max(nums[i]+solve(i+2), solve(i+1))
            dp[i] = curr
            return dp[i]
        return solve(0)