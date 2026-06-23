class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        ans = ""
        for i in range(len(s)):
            start = i
            j = len(s)-1
            while j > i:
                print(s[j], s[i])
                if s[j]!=s[i]:
                    j -= 1
                    continue
                while start<=j and s[j] == s[start]:
                    print('match found', s[j], s[start])
                    if len(s[i:j+1]) >= len(ans):
                        ans = s[i:j+1]
                    j -= 1
                    start += 1
        return ans