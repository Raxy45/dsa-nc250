class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(idx, val):
            if idx == len(nums):
                return 0
            
            if (idx, val) in dp:
                return dp[(idx, val)]
            
            curr = 0
            for i in range(idx, len(nums)):
                if nums[i] > val:
                    curr = max(curr, 1 + dfs(i+1, nums[i]))
            dp[(idx, val)] = curr
            return dp[(idx, val)]
        return dfs(0, float('-inf'))