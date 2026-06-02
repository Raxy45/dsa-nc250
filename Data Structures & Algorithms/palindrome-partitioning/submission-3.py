class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, subset = [], []
        def isPali(l, r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(idx):
            if idx==len(s):
                ans.append(subset.copy())
                return
            
            for i in range(idx, len(s)):
                if isPali(idx, i):
                    subset.append(s[idx:i+1])
                    dfs(i+1)
                    subset.pop()
        dfs(0)
        return ans