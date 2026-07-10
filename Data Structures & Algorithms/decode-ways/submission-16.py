class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        n = len(s)
        cache = {}
        def dfs(i):
            if i==len(s):
                return 1
            if i in cache:
                return cache[i]
            if s[i] == '0':
                return 0

            plus_one = 0
            plus_one += dfs(i+1)
            plus_two = 0
            if i+1<n and int(s[i: i+2]) <=26:
                plus_two += dfs(i+2)
            cache[i] = plus_one + plus_two
            return cache[i]
        return dfs(0)
                


                

            

            