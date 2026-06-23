class Solution:
    def is_alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a')<=ord(c)<=ord('z')) or (ord(1) <= ord(c) <= ord(0))
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        used_replace = False
        while l < r:
            while l<r and not self.is_alnum(s[l]):
                l+= 1
            while l<r and not self.is_alnum(s[r]):
                r-=1
            if s[l]!=s[r]:
                if used_replace:
                    return False
                if l+1<=r:
                    if s[l+1]==s[r]:
                        l+=1
                    else:
                        r-=1
                used_replace=True
            else:
                l+=1
                r-=1
                # if used_replace is False:
                #     used_replace = True
                #     r-=1
                # else:
                #     return False
            
        return True
