class Solution:
    def is_alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a')<=ord(c)<=ord('z')) or (ord(1) <= ord(c) <= ord(0))

    def validPalindrome(self, s: str) -> bool:
        def check(l, r, used_delete):
            while l < r:
                while l<r and not self.is_alnum(s[l]):
                    l+= 1
                while l<r and not self.is_alnum(s[r]):
                    r-=1
                if s[l]!=s[r]:
                    if used_delete:
                        return False
                    return check(l+1, r, True) or check(l, r-1, True)
                l+=1
                r-=1
            return True
        l, r = 0, len(s)-1
        return check(l, r, False)
