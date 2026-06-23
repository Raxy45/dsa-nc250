class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        char = ""
        dp = defaultdict(bool)
        def solve(i, char):
            print(i, char)
            if i==len(s):
                if len(char) == 0:
                    return True
                print('returned false for',i,char)
                return False
            
            # if i in dp: return dp[i]
            char += s[i]
            res = False
            if char in wordDict:
                print(char,'in wordDict')
                res = solve(i+1, "")
                if res:
                    # dp[i] = True
                    return res
            print('now solving for', char, 'idx', i)
            res = res or solve(i+1, char)
            # dp[i] = res
            return res
        
        wordDict = set(wordDict)
        return solve(0, "")