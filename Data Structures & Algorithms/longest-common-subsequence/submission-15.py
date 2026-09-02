class Solution:
    def longestCommonSubsequence(self, t1, t2):
        # Time Complexity: O(l1 * l2)
            # - We fill each cell of the dp table once.
            # - Total states = (l1 + 1) * (l2 + 1)

        # Space Complexity: O(l1 * l2)
            # - dp table stores results for all subproblems.
        l1, l2 = len(t1), len(t2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        dp = [0] * (l2+1)
        ans = 0
        diag = 0
        for i in range(l1-1, -1, -1):
            diag = 0
            for j in range(l2-1, -1, -1):
                temp = dp[j]
                if t1[i]==t2[j]:
                    # dp[i][j] = 1 + dp[i+1][j+1]
                    dp[j] = 1 + diag
                else:
                    # dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    dp[j] = max(dp[j], dp[j+1])
                diag = temp

        return dp[0]