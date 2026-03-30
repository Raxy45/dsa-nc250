class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = 0
        for length in range(1, len(s)+1):
            for i in range(0, (len(s)-length+1)):
                end_pointer = (i+length) - 1
                if length == 1:
                    dp[i][end_pointer] = True
                elif length == 2:
                    if s[i] == s[end_pointer]:
                        dp[i][end_pointer] = True
                else:
                    if s[i] == s[end_pointer] and dp[i+1][end_pointer-1]:
                        dp[i][end_pointer] = True
                
                if dp[i][end_pointer]:
                    ans += 1
        return ans