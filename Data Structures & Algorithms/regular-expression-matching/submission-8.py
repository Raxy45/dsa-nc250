class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)

        # nextdp = dp[i+1][*]
        nextdp = [False] * (pl + 1)
        nextdp[pl] = True

        # initialize empty string vs pattern
        for j in range(pl - 1, -1, -1):
            if j + 1 < pl and p[j + 1] == '*':
                nextdp[j] = nextdp[j + 2]

        for i in range(sl - 1, -1, -1):
            dp = [False] * (pl + 1)

            for j in range(pl - 1, -1, -1):
                match = p[j] == '.' or s[i] == p[j]

                if j + 1 < pl and p[j + 1] == '*':
                    # skip OR use
                    dp[j] = dp[j + 2] or (match and nextdp[j])
                elif match:
                    dp[j] = nextdp[j + 1]

            nextdp = dp

        return nextdp[0]

class Solution2DDP:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)
        dp = [ [False] * (pl+1) for _ in range(sl+1)]
        dp[sl][pl] = True
        for j in range(pl - 1, -1, -1):
            if (j+1)<pl and p[j+1] == '*':
                # check if we skipped current char, then from j+2 can we match empty strings?
                dp[sl][j] = dp[sl][j+2]
        for i in range(sl-1, -1, -1):
            for j in range(pl-1, -1, -1):
                match = p[j] == '.' or s[i] == p[j]
                if (j+1)<pl and p[j+1] == '*':
                    dp[i][j] = (dp[i][j+2] or (match and dp[i+1][j]))
                if not dp[i][j] and match:
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]

        

class SolutionRecMemo:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)
        dp = {}
        def solve(i, j):
            if j==pl:
                return i==sl
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            match = i<sl and (p[j] == '.' or s[i]==p[j])

            if (j+1)<pl and p[j+1] == '*':
                skip = solve(i, j+2)
                take = match and solve(i+1, j)
                dp[(i, j)] = skip or take
                return dp[(i, j)]
            
            if match:
                dp[(i, j)] = solve(i+1, j+1)
                return dp[(i, j)]
            
            dp[(i, j)] = False
            return dp[(i, j)]
        return solve(0, 0)
            