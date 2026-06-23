class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr_sentence = []
        wordDict_d = {key: True for key in wordDict}
        print(wordDict_d)
        def solve(i):
            if i==len(s):
                ans.append(" ".join(curr_sentence))
                return

            word = "" 
            for k in range(i, len(s)):
                word += s[k]
                if wordDict_d.get(word):
                    curr_sentence.append(word)
                    solve(k+1)
                    curr_sentence.pop()
        solve(0)
        return ans        
        