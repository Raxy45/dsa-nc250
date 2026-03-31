class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):          # O(n)
            for w in wordDict:                       # O(m)
                # substring comparison takes O(k)
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
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


