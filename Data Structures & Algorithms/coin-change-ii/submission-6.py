class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp  = {}
        def dfs(idx, remaining):
            if (idx, remaining) in dp: return dp[(idx, remaining)]

            if remaining == 0: return 1
            if remaining<0 or idx >= len(coins): return 0

            dp[(idx, remaining)] = dfs(idx, remaining - coins[idx]) + \
                                    dfs(idx+1, remaining)
            return dp[(idx, remaining)]
        return dfs(0, amount)