class Solution:
    def stoneGame(self, nums):
        n = len(nums)

        # dp[l] initially represents dp[l][l]
        dp = nums.copy()

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                take_left = nums[l] - dp[l + 1]
                take_right = nums[r] - dp[l]

                dp[l] = max(take_left, take_right)

        return dp[0] > 0
    def stoneGameR(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(start, end):
            if start==end:
                return piles[end]
            if (start, end) in dp: return dp[(start, end)]
            
            curr = float('-inf')
            dp[(start, end)] = max(curr, piles[start] - dfs(start+1, end), \
                        piles[end] - dfs(start, end-1))
            return dp[(start, end)]
        
        return True if dfs(0, len(piles)-1) > 0 else False