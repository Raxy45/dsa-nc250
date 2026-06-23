class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = defaultdict(bool)
        def solve(indx, curr_word):
            if indx == len(s):
                dp[indx] = True
                return dp[indx]
            
            if indx in dp:
                return dp[indx]
            
            curr_word += s[indx]
            if curr_word in wordDict:
                dp[indx+1] = solve(indx+1, "")
            dp[indx+1] = solve(indx+1, curr_word)
            return dp[indx+1]
        return solve(0, "")