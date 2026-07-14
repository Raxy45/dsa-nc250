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
            while idx<len(s):
                curr_s += s[idx]
                if curr_s in ds:
                    if dfs(idx+1):
                        cache[idx+1] = True
                        return cache[idx+1]
                idx += 1
            cache[idx] = False
            return cache[idx]
        return dfs(0)