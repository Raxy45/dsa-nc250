class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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