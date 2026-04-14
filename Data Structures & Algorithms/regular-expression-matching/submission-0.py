class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)

        def solve(i, j):
            if j == pl:
                return i == sl

            match = i < sl and (s[i] == p[j] or p[j] == '.')

            if j+1 < pl and p[j+1] == '*':
                return (
                    solve(i, j+2) or
                    (match and solve(i+1, j))
                )

            if match:
                return solve(i+1, j+1)

            return False

        return solve(0, 0)