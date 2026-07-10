class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        n = len(s)
        def dfs(i):
            if i==len(s):
                return 1
            if s[i] == '0':
                return 0

            plus_one = 0
            plus_one += dfs(i+1)
            plus_two = 0
            if i+1<n and int(s[i: i+2]) <=26:
                plus_two += dfs(i+2)
            return plus_one + plus_two
        return dfs(0)
                


                

            

            