class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)
        dp = {}
        def dfs(si, pi):
            if si==sl:
                if pi==pl:
                    return True
                return False
            
            if pi==pl: return False
            if (si,  pi) in dp:
                return dp[(si, pi)]
            
            curr = False
            if (pi+1) < pl and p[pi+1] == '*':
                if s[si] == p[pi] or p[pi] == '.':
                    curr = dfs(si+1, pi) or dfs(si+1, pi+2)
                else:
                    # chars do not match
                    curr = dfs(si, pi+2)
            elif p[pi] == '.' or s[si] == p[pi]:
                curr = dfs(si+1, pi+1)
            dp[(si, pi)] = curr
            return curr
                

        return dfs(0, 0)
        