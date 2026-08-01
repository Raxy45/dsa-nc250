class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        dp = {}
        def dfs(i, j):
            print(i, j)
            if i==len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s3[i+j] != s1[i] and s3[i+j] != s2[j]:
                dp[(i, j)] = False
            elif s1[i] == s3[i+j]:
                dp[(i, j)] = dfs(i+1, j)
            else:
                dp[(i, j)] = dfs(i, j+1)
            return dp[(i, j)]
        return dfs(0, 0)