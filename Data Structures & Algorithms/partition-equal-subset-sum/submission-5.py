class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)%2) > 0: return False
        t = sum(nums)//2
        dp = [[-1] * len(nums) for _ in range(t+1)]
        def solve(t, idx):
            if t==0:
                return True
            if idx>=len(nums):
                return False
            if dp[t][idx] != -1:
                return dp[t][idx]
            for i in range(idx, len(nums)):
                if t>=nums[i] and solve(t-nums[i], i+1):
                    dp[t][idx] = True
                    return True
            dp[t][idx] = False
            return dp[t][idx]
        return solve(t, 0)