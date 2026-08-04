class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s), len(p)
        dp = {}
        def dfs(si, pi):
            if pi==pl:
                if si==sl: return True
                return False
            # if pi==pl 
            if (si, pi) in dp:
                return dp[(si, pi)]
            
            curr = False
            match = si<sl and (s[si] == p[pi] or p[pi] == '.')
            if (pi + 1)<pl and p[pi+1] == '*':
                # special
                if match:
                    curr = dfs(si, pi+2) or dfs(si+1, pi)
                          # take one char using * and move ahead OR
                          # take one char of s, keep pi at same
                else:
                    # chars do not match. take zero chars from p
                    curr = dfs(si, pi+2)
            elif match:
                curr = dfs(si+1, pi+1)
            
            dp[(si, pi)] = curr
            return dp[(si, pi)]


        return dfs(0, 0)
        