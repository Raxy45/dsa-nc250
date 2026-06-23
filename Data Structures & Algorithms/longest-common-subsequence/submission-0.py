class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * l2 for _ in range(l1)]
        def solve(i, j):
            if i==l1 or j==l2:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + solve(i+1, j+1)
            
            return max(solve(i+1, j), solve(i, j+1))
        return solve(0, 0)