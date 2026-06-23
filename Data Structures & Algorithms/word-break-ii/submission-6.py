class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        ans, temp = [], []
        cache = defaultdict(list)

        def solve(idx, temp):
            print(f'{cache = }')
            print('solve called for', idx, temp)
            if idx == len(s):
                print('adding temp', temp,'to ans')
                ans.append(" ".join(temp))
                return

            if idx in cache:
                print('found idx in cache', idx)
                temp = temp + cache[idx]
                ans.append(" ".join(temp))
                return

            word = ""
            for i in range(idx, len(s)):
                word += s[i]
                if word in wordDict:
                    print('word', word)
                    temp.append(word)
                    cache[idx].append(word)
                    solve(i+1, temp)

                    temp.pop()
            if idx in cache:
                cache.pop(idx)
        solve(0, [])
        return ans