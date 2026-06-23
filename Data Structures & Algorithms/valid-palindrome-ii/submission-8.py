class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, used_delete) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                while l < r and not self.alphaNum(s[l]):
                    l += 1
                while r > l and not self.alphaNum(s[r]):
                    r -= 1
                print(s[l], s[r], used_delete)
                if s[l].lower() != s[r].lower():
                    if used_delete:
                        return False
                    return isPalindrome(s[l+1:r+1], True) or isPalindrome(s[l:r], True)
                l, r = l + 1, r - 1
            return True
        return isPalindrome(s, False)