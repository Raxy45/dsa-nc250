class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(l, r):
            if l == len(s): return True
            if (l, r) in dp:
                return dp[(l, r)]
            
            if r==len(p): return False
            curr = False
            if s[l] == p[r] or p[r] == '.':
                curr = dfs(l+1, r+1)
            elif p[r] != '*':
                curr = False
            else:
                # p[r] is * 
                curr = dfs(l+1, r+1) or dfs(l+1, r) or dfs(l, r+1)
            
            dp[(l, r)] = curr
            return dp[(l, r)]
        return dfs(0, 0)
        