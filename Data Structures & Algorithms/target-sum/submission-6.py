class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def solve(i, s):
            
            if i==n:
                if s==target:
                    return 1
                return 0
            
            if (i, s) in dp:
                return dp[(i, s)]
            # print(i, s, dp[i][s], 'before')
            dp[(i, s)] += solve(i+1, s+nums[i])
            # print(i, s, dp[i][s], 'mid')
            dp[(i, s)] += solve(i+1, s-nums[i])

            # print(i, s, dp[i][s], 'end')
            return dp[(i, s)]
        
        return solve(0, 0)


            

