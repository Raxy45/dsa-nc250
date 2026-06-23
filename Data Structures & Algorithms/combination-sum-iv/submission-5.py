class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for t in range(1, target+1):
            for n in nums:
                if t>=n:
                    dp[t] += dp[t-n]
        return dp[target]
    def combinationSum4TopDown(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # base case

        def solve(rem):
            if rem in dp:
                return dp[rem]

            count = 0
            for num in nums:
                if num <= rem:
                    count += solve(rem - num)

            dp[rem] = count
            return count

        return solve(target)