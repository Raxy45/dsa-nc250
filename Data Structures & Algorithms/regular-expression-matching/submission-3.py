class Solution:
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
            