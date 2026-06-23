class Solution:
    def rob(self, nums):
        dp = [0]*(len(nums)+1)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        print(dp)
        return dp[-2]
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