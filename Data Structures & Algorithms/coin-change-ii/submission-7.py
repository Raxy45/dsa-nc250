class Solution:
    def change(self, amt, cns):
        dp = [[0] * (amt+1) for _ in range(len(cns)+1)]

        for i in range(len(cns)+1):
            dp[i][0] = 1

        # print(dp)
        for i in range(len(cns)-1, -1, -1):
            for j in range(cns[i], amt+1):
                # print(i, cns[i], j)
                # print(dp)
                dp[i][j] = dp[i+1][j] + dp[i][j-cns[i]]
        return dp[0][amt]
    def changeRec(self, amount: int, coins: List[int]) -> int:
        dp  = {}
        def dfs(idx, remaining):
            if (idx, remaining) in dp: return dp[(idx, remaining)]

            if remaining == 0: return 1
            if remaining<0 or idx >= len(coins): return 0

            dp[(idx, remaining)] = dfs(idx, remaining - coins[idx]) + \
                                    dfs(idx+1, remaining)
            return dp[(idx, remaining)]
        return dfs(0, amount)