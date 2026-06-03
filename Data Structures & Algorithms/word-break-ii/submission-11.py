class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        cache = defaultdict(list)
        wordDict = set(wordDict)
        def dfs(i):
            # print('CURRENT I', i)
            if i==len(s):
                return [""]
            
            if i in cache:
                return cache[i]
            
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if curr in wordDict:
                    string_from_j = dfs(j+1)
                    for output in string_from_j:
                        temp = curr
                        if output:
                            temp = curr + " " + output
                        cache[i].append(temp)
            return cache[i]
        return dfs(0)
            
        