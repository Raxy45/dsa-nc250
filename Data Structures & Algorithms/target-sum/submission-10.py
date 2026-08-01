class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(idx, curr_sum):
            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]
            if idx == len(nums):
                if curr_sum == target:
                    return 1
                return 0
            
            dp[(idx, curr_sum)] = dfs(idx+1, curr_sum + nums[idx]) + \
                                  dfs(idx+1, curr_sum - nums[idx])
            return dp[(idx, curr_sum)]
        return dfs(0, 0)

        