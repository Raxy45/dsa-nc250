class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(l, r):
            if (l, r) in dp: return dp[(l, r)]
            if l==len(word1) and r==len(word2): return 0
            if l==len(word1):
                return len(word2) - r
            if r==len(word2):
                return len(word1) - l
            
            curr = float('inf')
            if word1[l] == word2[r]:
                curr = dfs(l+1, r+1)
            else:
                curr = 1 + min(dfs(l+1, r), #delete 
                               dfs(l+1, r+1), # replace
                               dfs(l, r+1) # insert
                               )
            dp[(l, r)] = curr
            return dp[(l, r)]
        return dfs(0, 0)
            
        