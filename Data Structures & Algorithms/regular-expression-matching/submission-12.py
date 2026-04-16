class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)

        dp = [False] * (pl + 1)
        dp[pl] = True

        # initialize empty string row
        for j in range(pl - 1, -1, -1):
            if j + 1 < pl and p[j + 1] == '*':
                dp[j] = dp[j + 2]

        for i in range(sl - 1, -1, -1):
            prev = dp[pl]   # this is dp[i+1][pl]
            dp[pl] = False  # dp[i][pl] = False

            for j in range(pl - 1, -1, -1):
                temp = dp[j]  # store dp[i+1][j]

                match = p[j] == '.' or s[i] == p[j]

                if j + 1 < pl and p[j + 1] == '*':
                    dp[j] = dp[j + 2] or (match and temp)
                else:
                    dp[j] = match and prev

                prev = temp  # move diagonal

        return dp[0]
        
class Solution1DDP:
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
            if j == pl:
                return i == sl

            if (i, j) in dp: return dp[(i, j)]
            match = i < sl and (s[i] == p[j] or p[j] == '.')

            if j+1 < pl and p[j+1] == '*':
                dp[(i, j)] = (
                    solve(i, j+2) or
                    (match and solve(i+1, j))
                )
                return dp[(i, j)]
            if match:
                dp[(i, j)] = solve(i+1, j+1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return dp[(i, j)]

        return solve(0, 0)

class SolutionRec:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)

        def solve(i, j):
            if j == pl:
                if i==sl:
                    return True
                return False
            
            match = i<sl and (s[i]==p[j] or p[j] == '.')
            
            if (j+1)<pl and p[j+1] == '*':
                not_take = solve(i, j+2) # skipped a* from a*b -> directly jump to b
                take = (match and solve(i+1, j)) # if curr char matches and next is * -> move i ahead by one and solve
                return take or not_take
            
            if match:
                # just match, without asterick
                return solve(i+1, j+1)
            return False
        return solve(0, 0)