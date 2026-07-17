class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for curr_target in range(target+1):
            for i in range(len(nums)):
                if (curr_target - nums[i]) < 0: continue
                dp[curr_target] += dp[curr_target - nums[i]]
        return dp[target]
    def combinationSum4TopDown(self, nums: List[int], target: int) -> int:
        cache = {}
        # cache[k] = j # represents there are j ways to 
        # get sum==k

        def dfs(req):
            if req<0: return 0
            if req == 0: return 1
            if req in cache: return cache[req]

            cache[req] = 0
            for i in range(len(nums)):
                cache[req] += dfs(req - nums[i])
            return cache[req]
        return dfs(target)