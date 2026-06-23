class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        cache = defaultdict(list)
        wordDict = set(wordDict)
        def dfs(i):
            print('CURRENT I', i)
            if i==len(s):
                return [""]
            
            if i in cache:
                return cache[i]
            
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if curr in wordDict:
                    print('Word', curr, 'exists in dict')
                    string_from_j = dfs(j+1)
                    print('strings starting from', j+1, 'are', string_from_j)
                    for output in string_from_j:
                        cache[i].append(curr+" "+output.strip())
            print('wordsFormed for', i, 'are', cache[i])
            return cache[i]
        output = dfs(0)
        print(output)
        return output
            
        