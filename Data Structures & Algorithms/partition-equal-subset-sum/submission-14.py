class Solution:
    def canPartition(self, nums):
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = int(arr_sum/2)
        n = len(nums)
        dp = [[False] * (req_sum+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        
        for idx in range(n-1, -1, -1):
            for j in range(nums[idx], req_sum+1):
                dp[idx][j] = dp[idx+1][j-nums[idx]] or dp[idx+1][j]
                # dp[idx][target] = dp[idx+1][target] 
                # if (target - nums[idx]) >=0 :
                #     dp[idx][target] = dp[idx][target] or dp[idx+1][target-nums[idx]]
        return dp[0][req_sum]

    def canPartition2(self, nums):
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = int(arr_sum/2)
        n = len(nums)
        next_elem, curr_elem = [False] * (req_sum+1), [False] * (req_sum+1)
        next_elem[0] = curr_elem[0] = True
        
        for idx in range(n-1, -1, -1):
            for target in range(req_sum, 0, -1):
                curr_elem[target] = next_elem[target] 
                if (target - nums[idx]) >=0 :
                    curr_elem[target] = curr_elem[target] or next_elem[target-nums[idx]]
            next_elem, curr_elem = curr_elem.copy(), [False] * (req_sum+1)
            curr_elem[0] = True
        return next_elem[req_sum]
        
    def canPartition2DDP(self, nums):
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = int(arr_sum/2)
        n = len(nums)
        dp = [[False] * (req_sum+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        
        for idx in range(n-1, -1, -1):
            for target in range(req_sum, 0, -1):
                dp[idx][target] = dp[idx+1][target] 
                if (target - nums[idx]) >=0 :
                    dp[idx][target] = dp[idx][target] or dp[idx+1][target-nums[idx]]
        return dp[0][req_sum]
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

        