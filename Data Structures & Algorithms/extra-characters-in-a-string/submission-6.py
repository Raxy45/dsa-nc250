class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        cache = {len(s): 0}
        def dfs(i):
            if i in cache: return cache[i]
            if i == len(s):
                return 0
            
            res = 1 + dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, dfs(j+1))
            cache[i] = res
            return res
        return dfs(0)