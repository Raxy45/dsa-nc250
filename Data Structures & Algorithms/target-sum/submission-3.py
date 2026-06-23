class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [ [0] * (sum(nums)+1) for _ in range(n+1)]
        def solve(i, s):
            
            if i==n:
                if s==target:
                    return 1
                return 0
            
            print(i, s, dp[i][s], 'before')
            dp[i][s] += solve(i+1, s+nums[i])
            print(i, s, dp[i][s], 'mid')
            dp[i][s] += solve(i+1, s-nums[i])

            print(i, s, dp[i][s], 'end')
            return dp[i][s]
        
        return solve(0, 0)


            

