class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s):0}
        def dfs(idx):
            if idx in dp: return dp[idx]
            res = 1 + dfs(idx + 1)

            for j in range(idx, len(s)):
                if s[idx:j+1] in dictionary:
                    res = min(res, dfs(j+1))
            dp[idx] = res
            return res
        return dfs(0)