class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        char = ""
        dp = defaultdict(bool)
        def solve(i, char):
            if i==len(s) and char == "":
                return True
            
            if i in dp: return dp[i]
            char += s[i]
            res = False
            if char in wordDict:
                res = solve(i+1, "")
            res = res or solve(i+1, char)
            dp[i] = res
            return res
        
        wordDict = set(wordDict)
        return solve(0, "")