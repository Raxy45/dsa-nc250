class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            if i in cache:
                print('already found word beginning from', i, 'in cache')
                return cache[i]

            res = []
            w = ""
            for j in range(i, len(s)):
                w += s[j]
                if w not in wordDict:
                    continue
                
                print('current word', w)
                strings = backtrack(j + 1)
                print('Adding strings', strings, ' starting from j+1', j+1, 'with word', w)
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
                print('cache inner', cache)
                print('current res', res)
                print('*'*3)
            cache[i] = res
            print(cache)
            print('*'*9)
            return res

        backtrack(0)
        return cache[0]