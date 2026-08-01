class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        dp = {(len(s1), len(s2)) : True}
        def dfs(i, j):
            if(i, j) in dp: return dp[(i, j)]
            
            curr = False
            if i<len(s1) and s1[i] == s3[i+j]:
                curr = dfs(i+1, j)
            if not curr and j<len(s2) and s2[j] == s3[i+j]:
                curr = dfs(i, j+1)
            dp[(i, j)] = curr
            return dp[(i, j)]
        return dfs(0, 0)