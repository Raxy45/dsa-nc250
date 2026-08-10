class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i+minJump, farthest+1)
            for j in range(start, min(len(s), i + maxJump+1)):
                if s[j] == '0':
                    q.append(j)
                    if j == (len(s) - 1):
                        return True
            farthest = i + maxJump
        return False

    def canReach1D(self, s: str, minJump: int, maxJump: int) -> bool:
        def dfs(i):
            # print(i, j)
            if (i) in dp:
                return dp[i]
            if i == (len(s)-1):
                return True
            j = i +1
            while j<len(s):
                if s[j] == '0' and (i+minJump) <= j and j<=min(i+maxJump, len(s)-1):
                    dp[i] = dfs(j)
                    if dp[i]: return True
                j += 1
            dp[i] = False
            return dp[i]
        dp = {}
        return dfs(0)
        