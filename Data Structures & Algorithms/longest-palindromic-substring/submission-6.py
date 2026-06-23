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
        n = len(s)

        maxL = 0
        index = 0

        # t[i][j] = True if s[i..j] is a palindrome
        t = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        maxL = 1
        for i in range(n):
            t[i][i] = True

        # L = length of substring
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if s[i] == s[j] and L == 2:
                    t[i][j] = True
                    maxL = 2
                    index = i

                elif s[i] == s[j] and t[i + 1][j - 1]:
                    t[i][j] = True
                    if L > maxL:
                        maxL = L
                        index = i
                else:
                    t[i][j] = False

        return s[index:index + maxL]