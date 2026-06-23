class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(s_i):
            if s_i == len(s):
                return True
            
            if s_i in dp:
                return dp[s_i]
            
            for j in range(s_i, len(s)):
                if s[s_i:j+1] in wordDict:
                    if solve(j+1):
                        # start with new empty word
                        dp[j+1] = True
                        return True
            return False
        dp = defaultdict(bool)
        return solve(0)