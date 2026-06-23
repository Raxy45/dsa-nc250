class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        w_s = set(wordDict)
        ans, c_ws = [], []
        def solve(idx):
            if idx == len(s):
                ans.append(" ".join(c_ws))
                return
            
            current_w = ""
            for i in range(idx, len(s)):
                current_w += s[i]
                if current_w in wordDict:
                    c_ws.append(current_w)
                    solve(i+1)
                    c_ws.pop()
        solve(0)
        return ans