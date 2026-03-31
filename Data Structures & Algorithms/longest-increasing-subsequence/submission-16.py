class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
        # print(dp)
        return ans