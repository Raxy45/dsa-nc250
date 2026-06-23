class SolutionBottomUP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[len(nums)-1] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], 1+dp[i])
        return max(dp)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def solve(i):
            if i in dp:
                return dp[i]

            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + solve(j))

            dp[i] = res
            return res

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans