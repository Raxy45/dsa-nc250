class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def solve(idx):
            if idx==len(s):
                ans.append(part.copy())
                return
            
            for i in range(idx, len(s)):
                if isValidPali(s, idx, i):
                    part.append(s[idx:i+1])
                    solve(i+1)
                    part.pop()
        def isValidPali(w, l, r):
            while l<r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True
        
        ans, part = [], []
        solve(0)
        return ans
                    