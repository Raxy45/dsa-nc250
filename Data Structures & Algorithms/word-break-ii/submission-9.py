class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        subset = []
        wordDict = set(wordDict)
        def dfs(i):
            if i==len(s):
                ans.append(" ".join(subset.copy()))
                return
            
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if curr in wordDict:
                    subset.append(s[i:j+1])
                    dfs(j+1) # split
                    subset.pop()
        dfs(0)
        return ans
            
        