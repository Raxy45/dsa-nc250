class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(int)
        dp[len(s)] = True
        def solve(idx):
            if idx in dp:
                return dp[idx]
            for i in range(idx, len(s)):
                if s[idx: i+1] in wordDict:
                    if solve(i+1):
                        dp[idx] = True
                        return dp[idx]
               
            dp[idx] = False
            return dp[idx]
        return solve(0)


