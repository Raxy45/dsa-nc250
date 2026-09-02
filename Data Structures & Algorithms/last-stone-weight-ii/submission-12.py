class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # capacity = total_sum / 2

        # For each stone:
        #     take it if it fits
        #     OR don't take it

        # Goal:
        #     maximize the amount we can fill
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
            
            # max(take, not_take) 

            # not_take
            curr = dfs(idx+1, curr_sum)
            if stones[idx]<=curr_sum:
                take = stones[idx] + dfs(idx+1, curr_sum-stones[idx])
                curr = max(curr, take)
            dp[(idx, curr_sum)] = curr
            return dp[(idx, curr_sum)]

        half = dfs(0, req_sum)
        # print(half)
        return (total_sum - 2*half)
            
        
class SolutionDifferentApproach:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum) // 2
        dp = {}

        # Solution present in book

        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            
            if total>=target or i==len(stones):
                return abs(stoneSum-2*total)
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
            return dp[(i, total)]
        return dfs(0, 0)