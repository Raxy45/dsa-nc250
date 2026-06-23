class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        dp = defaultdict(int)
        def solve(target):
            nonlocal ans
            if target == 0:
                return 1
            
            if target in dp:
                return dp[target]
            curr_count = 0
            for n in nums:
                if n<=target:
                    curr_count += solve(target-n)
            dp[target] = max(dp[target], curr_count)
            return dp[target]
        solve(target)
        return dp[target]