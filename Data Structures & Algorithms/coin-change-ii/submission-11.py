class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        n = len(coins)
        dp = {}
        def dfs(idx, remaining):
            if (idx, remaining) in dp:
                return dp[(idx, remaining)]
            if remaining == 0:
                return 1
            if idx == n:
                return 0
            
            curr = 0
            for i in range(idx, n):
                if coins[i]>remaining:
                    continue
                curr += dfs(i, remaining-coins[i])
            dp[(idx, remaining)] = curr
            return dp[(idx, remaining)]
        return dfs(0, amount)