class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        wds =set(wordDict)
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            
            curr = ""
            matched = False
            for i in range(idx, len(s)):
                curr += s[i]
                if curr in wordDict:
                    matched = dfs(i+1)
                    if matched:
                        break
            dp[idx] = matched
            return dp[idx]
        return dfs(0)

