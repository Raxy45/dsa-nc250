class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<=r:
            while l<r and not s[l].isalpha():
                l += 1
            while r>l and not s[r].isalpha():
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True