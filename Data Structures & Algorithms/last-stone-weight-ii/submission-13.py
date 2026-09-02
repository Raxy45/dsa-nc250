from typing import List


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

    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # dp[i][s] =
        # maximum subset sum <= s using stones[i:]

        for i in range(n - 1, -1, -1):
            for s in range(target + 1):

                # Don't take stones[i]
                not_take = dp[i + 1][s]

                # Take stones[i]
                take = 0
                if stones[i] <= s:
                    take = stones[i] + dp[i + 1][s - stones[i]]

                dp[i][s] = max(take, not_take)

        half = dp[0][target]

        return total_sum - 2 * half

    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        dp = [0] * (target + 1)

        for stone in stones:
            for s in range(target, stone - 1, -1):
                dp[s] = max(
                    dp[s],
                    stone + dp[s - stone]
                )

        half = dp[target]

        return total_sum - 2 * half