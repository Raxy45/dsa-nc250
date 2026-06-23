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
    def solve(self, s, l, r, dp):
        if dp[l][r]:
            return True
        start, end = l, r
        while l <= r:
            if s[l] != s[r]:
                dp[l][r] = False
                return False
            l += 1
            r -= 1
        dp[start][end] = True
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] 
        max_len = float('-inf')
        starting_index = 0

        for i in range(n):
            for j in range(i, n):
                if self.solve(s, i, j, dp):
                    if (j - i + 1) > max_len:
                        starting_index = i
                        max_len = j - i + 1

        return s[starting_index: starting_index + max_len]