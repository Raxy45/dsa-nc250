class Solution:
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