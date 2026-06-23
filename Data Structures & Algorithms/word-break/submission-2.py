class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = defaultdict(bool)
        subs = ""
        def solve(indx):
            nonlocal dp, subs
            print(indx, dp)
            if indx == len(s):
                dp[indx] = True
                return dp[indx]
            
            if indx in dp:
                return dp[indx]
            
            if s[:indx] in wordDict:
                print('found match of', s[:indx])
                dp[indx+1] = solve(indx+1)
                if dp[indx+1]:
                    return True
            dp[indx+1] = solve(indx+1)
            return dp[indx+1]
        solve(0)
        return dp[len(s)]