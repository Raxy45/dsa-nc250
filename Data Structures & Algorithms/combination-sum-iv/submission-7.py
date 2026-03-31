class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        dp = defaultdict(int)
        dp[0] = 1
        def solve(t):
            nonlocal ans
            if t in dp:
                return dp[t]
            
            for i in range(len(nums)):
                if t>=nums[i]:
                    dp[t] += solve(t-nums[i])
            return dp[t]
        return solve(target)