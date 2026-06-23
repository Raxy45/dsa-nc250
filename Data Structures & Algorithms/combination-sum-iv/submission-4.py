class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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