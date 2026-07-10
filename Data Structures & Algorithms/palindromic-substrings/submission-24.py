class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for l in range(1, n+1):
            for i in range(n+1-l):
                j = i+l-1
                # print(i, j, l, n+l-1)
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j]:
                    count += 1
            # print('l', dp)
        # print(dp)
        return count