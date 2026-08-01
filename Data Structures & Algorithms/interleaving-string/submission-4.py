class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        def dfs(i, j):
            print(i, j)
            if i==len(s1) and j == len(s2):
                return True
            
            if s3[i+j] != s1[i] and s3[i+j] != s2[j]:
                return False
            if s1[i] == s3[i+j]:
                return dfs(i+1, j)
            else:
                return dfs(i, j+1)
            return False
        return dfs(0, 0)