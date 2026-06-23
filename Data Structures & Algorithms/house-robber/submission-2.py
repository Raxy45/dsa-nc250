class Solution:
    def rob(self, nums: List[int]) -> int:
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