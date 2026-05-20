class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l, r = 0, 0
        ans = ""
        while l<len(w1) or r<len(w2):
            if l<len(w1):
                ans += w1[l]
                l += 1
            
            if r<len(w2):
                ans += w2[r]
                r += 1
        return ans
        