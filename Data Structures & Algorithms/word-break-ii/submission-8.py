class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        w_s = set(wordDict)
        ans, c_ws = [], []
        def solve(idx):
            if idx == len(s):
                return [""]
            
            if idx in cache:
                return cache[idx]

            current_w = ""
            current_ws = []
            for i in range(idx, len(s)):
                current_w += s[i]
                if current_w not in wordDict:
                    continue
                
                words_formed_after_i = solve(i+1)
                for word in words_formed_after_i:
                    sentence = current_w
                    if word:
                        sentence = sentence + " " + word
                    current_ws.append(sentence)
            cache[idx] = current_ws
            return current_ws
        cache = {}
        solve(0)
        return cache[0]