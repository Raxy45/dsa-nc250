class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        dp = {}
        def dfs(si, sj):
            if (si, sj) in dp:
                return dp[(si, sj)]
            # print(si, sj)
            if (si+sj) == len(s3):
                return True
            if si==len(s1) and sj==len(s2):
                return False
            
            if si<len(s1) and s1[si] == s3[si+sj]:
                if (dfs(si+1, sj)):
                    return True

            if sj<len(s2) and s2[sj] == s3[si+sj]:
                if dfs(si, sj+1):
                    return True
            dp[(si, sj)] = False
            return dp[(si, sj)]
        return dfs(0, 0)