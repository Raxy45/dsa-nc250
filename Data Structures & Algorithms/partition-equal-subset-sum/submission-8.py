class Solution:
    def canPartition(self, nums):
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = int(arr_sum/2)
        n = len(nums)
        dp = [[False] * (req_sum+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = True
        
        for idx in range(n-1, -1, -1):
            for target in range(req_sum, 0, -1):
                dp[idx][target] = dp[idx+1][target] 
                if (target - nums[idx]) >=0 :
                    # if idx==1 and target == 4:
                        # print(idx+1, target-nums[idx], dp[idx+1][target-nums[idx]], dp[idx+1][target])
                    dp[idx][target] = dp[idx][target] or dp[idx+1][target-nums[idx]]
                # print('i, t', idx, target, dp[idx][target])
        for i in range(n):
            # print(i, req_sum)
            if dp[i][req_sum]: return True
        # print(dp)
        return False
    def canPartitionTopDown(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = arr_sum/2
        cache = {}
        def dfs(idx, curr):
            if curr == 0: return True
            if curr <0 or idx==len(nums): return False
            if (curr, idx) in cache: return cache[(curr, idx)]

            cache[(curr, idx)] = dfs(idx+1, curr-nums[idx]) or dfs(idx+1, curr)
            return cache[(curr, idx)]
        return dfs(0, req_sum)

        