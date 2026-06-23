class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        si, ti = 0, 0
        sl, tl = len(s), len(t)
        dp = {}
        def solve(si, ti):
            if ti == tl:
                return 1
            
            if si==sl:
                return 0
            
            if (si, ti) in dp:
                return dp[(si, ti)]
            take = 0
            if s[si] == t[ti]:
                # take
                take = solve(si+1, ti+1)
            not_take = solve(si+1, ti)
            dp[(si, ti)] = take + not_take
            return dp[(si, ti)]
        return solve(0, 0)