class Solution:
    def stoneGame(self, nums):
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)

        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # base case: length = 1
        for i in range(n):
            dp[i][i] = nums[i]

        # fill for lengths 2 → n
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                dp[l][r] = max(
                    nums[l] - dp[l+1][r],
                    nums[r] - dp[l][r-1]
                )

        return dp[0][n-1] > 0
    def stoneGameRecMemo(self, nums: List[int]) -> bool:
        dp = defaultdict(int)
        def solve(l, r):
            if l>r: return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = max(nums[l]-solve(l+1, r), nums[r]-solve(l, r-1))
            return dp[(l, r)]
        # print(solve(0, len(nums)-1))
        
        return True if solve(0, len(nums)-1) > 0 else False