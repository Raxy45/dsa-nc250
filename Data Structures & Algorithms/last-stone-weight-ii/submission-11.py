class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        req_sum = total_sum // 2
        dp = {}
        def dfs(idx, curr_sum):
            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]

            if curr_sum == 0:
                return 0
            if idx == len(stones):
                return 0
            
            # min(take, not_take) 
            curr = dfs(idx+1, curr_sum)
            if stones[idx]<=curr_sum:
                curr = max(curr, stones[idx] + dfs(idx+1, curr_sum - stones[idx]))
            dp[(idx, curr_sum)] = curr
            return dp[(idx, curr_sum)]

        half = dfs(0, req_sum)
        print(half)
        return (total_sum - 2*half)
            
        # ÷return dfs(sum(stones))