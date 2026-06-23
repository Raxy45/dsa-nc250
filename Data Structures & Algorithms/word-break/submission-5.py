class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}

        def solve(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]

            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and solve(j+1):
                    dp[i] = True
                    return True

            dp[i] = False
            return False

        return solve(0)