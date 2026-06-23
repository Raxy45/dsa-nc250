class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def solve(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]

            ways = solve(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += solve(i + 2)

            dp[i] = ways
            return ways

        return solve(0)