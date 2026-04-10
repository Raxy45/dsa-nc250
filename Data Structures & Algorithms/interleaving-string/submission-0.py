class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, N = len(s1), len(s2), len(s3)

        # Important check
        if m + n != N:
            return False

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def solve(i, j):
            if i == m and j == n:
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            # try taking from s1
            if i < m and s1[i] == s3[i + j]:
                if solve(i + 1, j):
                    dp[i][j] = True
                    return True

            # try taking from s2
            if j < n and s2[j] == s3[i + j]:
                if solve(i, j + 1):
                    dp[i][j] = True
                    return True

            dp[i][j] = False
            return False

        return solve(0, 0)