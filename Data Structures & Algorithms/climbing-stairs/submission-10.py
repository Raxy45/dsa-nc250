class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        def dfs(i):
            if i in cache: return cache[i]
            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]
        return dfs(n)

        