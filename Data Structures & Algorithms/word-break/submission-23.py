class Solution:
    def wordBreak(self, s, wordDict):
        ds = set(wordDict)
        mp = [False] * (len(s)+1)
        mp[len(s)] = True
        curr = ""
        # for i in range(len(s)-1, -1, -1):
        #     curr = s[i] + curr
        #     print(curr)
        #     if curr in wordDict:
        #         mp[i] = mp[i+len(curr)]
        #     if mp[i]:
        #         curr = ""
        n = len(s)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in ds and mp[j+1]:
                    mp[i] = True
                    break
        return mp[0]
    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        ds = set(wordDict)

        def dfs(idx):
            if idx == len(s):
                return True
            if idx in cache:
                return cache[idx]

            curr_s = ""
            start = idx
            while idx<len(s):
                curr_s += s[idx]
                if curr_s in ds:
                    if dfs(idx+1):
                        cache[start] = True
                        return cache[start]
                idx += 1
            cache[start] = False
            return cache[start]
        return dfs(0)