class SolutionBF:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # odd length
            temp = expand(i, i)
            if len(temp) > len(res):
                res = temp

            # even length
            temp = expand(i, i+1)
            if len(temp) > len(res):
                res = temp

        return res

class SolutionIdeal:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        maxL = 0
        index = 0

        # t[i][j] = True if s[i..j] is a palindrome
        t = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        maxL = 1
        for i in range(n):
            # This means every single char in string is palindrome
            # i.e. t[0][0] = True, t[1][1] = True  
            t[i][i] = True

        # L = length of substring
        for L in range(2, n + 1):
            # Example: l=2, find all substrings of length 2
            for i in range(n+1 - L):
                # j indicates the ending position, i.e char standing at end of length
                # example: str = sade l = 2, i = 0 then j =0+2-1 -> j=1 -> "a" 
                j = i + L - 1

                if s[i] == s[j] and L == 2:
                    # Now when s[i] == s[j]
                    # since length is already 2 -> and both the chars match therefore mark True
                    t[i][j] = True
                    maxL = 2
                    index = i

                elif s[i] == s[j] and t[i + 1][j - 1]:
                    # this means suppose you have ababa -> then centre a already marked True
                    # b at 1st and b at 3rd both are same -> and innner char i.e. i+1 and j-1 -> True
                    # therefore consider bab as True
                    # L earlier was 1, now 2 -> update maxLen and store the starting index
                    t[i][j] = True
                    if L > maxL:
                        maxL = L
                        index = i
                else:
                    t[i][j] = False

        return s[index:index + maxL]