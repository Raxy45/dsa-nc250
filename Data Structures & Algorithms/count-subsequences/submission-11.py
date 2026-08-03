class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl, tl = len(s), len(t)
        dp = [1] * (sl+1)
        # dp[sl] = 0
        
        # dp[i][j] represents number of distinct subsequence we can get from s[j:] to build t[i:]
        for ti in range(tl - 1, -1, -1):
            diag = dp[sl]     # old dp[ti+1][sl]


            dp[sl] = 0        # dp[i][sl]

            for si in range(sl - 1, -1, -1):
                temp = dp[si]             # old dp[i+1][si]

                dp[si] = dp[si + 1]       # skip s[si]

                if s[si] == t[ti]:
                    dp[si] += diag        # use old dp[i+1][si+1]

                diag = temp               # next diagonal
        return dp[0]

    def numDistinct2D(self, s: str, t: str) -> int:
        sl, tl = len(s), len(t)
        dp = [[0] * (sl+1) for _ in range(tl+1)]

        for i in range(sl+1):
            dp[tl][i] = 1
        
        # dp[i][j] represents number of distinct subsequence we can get from s[j:] to build t[i:]
        for ti in range(tl-1, -1, -1):
            for si in range(sl-1, -1, -1):
                dp[ti][si] = dp[ti][si+1] # -> This represents if we skipped current char of s, \
                                        # then can we obtain t from s[si+1:]
                
                if s[si] == t[ti]:
                    # if current chars match, then if we took both chars from s and t
                    # then check if from s[si+1:] can we get t[ti+1:] -> add the number of ways to current (ti, si)
                    dp[ti][si] += dp[ti+1][si+1]
        return dp[0][0]