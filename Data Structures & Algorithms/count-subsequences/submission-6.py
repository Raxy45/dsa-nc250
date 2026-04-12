class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        si, ti = 0, 0
        sl, tl = len(s), len(t)
        dp = [[0]*(tl+1) for _ in range(sl+1)]
        dp[sl][tl] = 1 # when no elements from s and t are present -> 1 way to get this subsequence
        # print(dp)
        for i in range(sl+1):
            dp[i][tl] = 1
        for i in range(sl-1, -1, -1):
            for j in range(tl-1, -1, -1):
                take = 0
                if s[i] == t[j]:
                    take = dp[i+1][j+1] # move i by 1 and j by 1 -> does with given elems you can form subsequence?
                not_take = dp[i+1][j] # skip current char and move down -> with s[i+1:] you can form t[j:]?
                dp[i][j] = take + not_take
        # print(dp)
        return dp[0][0]
        # dp[0][0] -> means number of subsequences with which you can form t from s
        
        def solve(si, ti):
            if ti == tl:
                return 1
            
            if si==sl or (sl-si)<(tl-ti):
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
class SolutionRecMemo:
    def numDistinct(self, s: str, t: str) -> int:
        si, ti = 0, 0
        sl, tl = len(s), len(t)
        dp = {}
        def solve(si, ti):
            if ti == tl:
                return 1
            
            if si==sl or (sl-si)<(tl-ti):
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