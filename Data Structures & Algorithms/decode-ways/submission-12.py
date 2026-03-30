class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if int(s[i]) == 0:
                continue
            dp[i] = dp[i+1]
            if (i+2)<=n and int(s[i:i+2])<27:
                dp[i] += dp[i+2]
        return dp[0]
    def numDecodingsTopDownMemo(self, s: str) -> int:
        ans = 0
        dp = defaultdict(int)
        dp[len(s)] = 1
        def solve(i):
            nonlocal ans
            # print(i)
            if i in dp:
                return dp[i]
            
            if int(s[i])<=0: return 0
            dp[i] += solve(i+1)

            if (i+1)<len(s) and int(s[i:i+2])<27:
                # print('called from', i)
                dp[i] += solve(i+2)
            # print('here for', i)
            return dp[i]
        return solve(0)