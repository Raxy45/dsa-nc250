class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = defaultdict(bool)
        def solve(indx, curr_word):
            nonlocal dp
            print(indx, curr_word, dp)
            if indx == len(s):
                if curr_word == "":
                    print(f'setting indx {indx} to Troe')
                    dp[indx] = True
                    return dp[indx]
                print(f'setting indx {indx} to False')
                return False
            
            if indx in dp:
                return dp[indx]
            
            curr_word += s[indx]
            if curr_word in wordDict:
                print('found match of', curr_word)
                dp[indx+1] = solve(indx+1, "")
                if dp[indx+1]:
                    return True
            dp[indx+1] = solve(indx+1, curr_word)
            return dp[indx+1]
        solve(0, "")
        return dp[len(s)]