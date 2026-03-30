class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(l, r):
            count = 0
            while(l>=0 and r<n and s[l]==s[r]):
                count += 1
                l -= 1
                r += 1
            return count
        
        ans = 0
        n = len(s)
        for i in range(len(s)):
            ans += check(i, i) # odd
            ans += check(i, i+1)    # tc
        return ans