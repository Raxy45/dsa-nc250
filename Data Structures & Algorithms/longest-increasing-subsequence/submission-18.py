class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        dp[len(nums)-1] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], 1+dp[i])
        print(dp)
        return max(dp)
    def lengthOfLISTopDown(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        dp[len(nums)] = 0
        ans = 1
        def solve(idx):
            nonlocal ans
            if idx in dp:
                return dp[idx]
            
            res = 1
            for i in range(idx+1, len(nums)):
                if nums[i] > nums[idx]:
                    res = max(res, 1+solve(i))
            dp[idx] = res
            return dp[idx]
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans