class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def checkPali(l, r):
            print('for index', l, r)
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            print('ans is', s[l:r+1])
            return s[l+1:r]
        ans = ""
        for i in range(n):
            s1 = checkPali(i, i)
            if len(s1) > len(ans):
                ans = s1
            

            s2 = checkPali(i, i+1)
            if len(s2) > len(ans):
                ans = s2
        return ans