class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        curr = [0] * (n+1)
        for i in range(m-1, -1, -1):
            diag = 0
            for j in range(n-1, -1, -1):
                temp = curr[j]
                if text1[i] == text2[j]:
                    curr[j] = 1 + diag
                else:
                    curr[j] = max(curr[j], curr[j+1])
                diag = temp
        return curr[0]