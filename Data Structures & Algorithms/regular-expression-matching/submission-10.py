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

class Solution:
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