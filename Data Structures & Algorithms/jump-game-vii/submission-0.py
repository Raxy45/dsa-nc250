class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        def dfs(i, j):
            # print(i, j)
            if (i, j) in dp:
                return dp[(i, j)]
            if i == (len(s)-1):
                return True
            while j<len(s):
                if s[j] == '0' and (i+minJump) <= j and j<=min(i+maxJump, len(s)-1):
                    dp[(i, j)] = dfs(j, j+1)
                    if dp[(i, j)]: return True
                j += 1
            return False
        dp = {}
        return dfs(0, 1)
        