class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        def dfs(i, j):
            # print(i, j)
            if i==len(s1) and j == len(s2):
                return True
            
            if (i<len(s1)) and s3[i+j] != s1[i] and j<len(s2) and s3[i+j] != s2[j]:
                return False
            
            curr = False
            if i<len(s1) and s1[i] == s3[i+j]:
                if dfs(i+1, j): return True
            if j<len(s2) and s2[j] == s3[i+j]:
                return dfs(i, j+1)
            return False
        return dfs(0, 0)