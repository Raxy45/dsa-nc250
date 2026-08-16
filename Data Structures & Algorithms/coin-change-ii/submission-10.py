class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        n = len(coins)
        dp = {}
        def dfs(idx, remaining):
            # print(remaining)
            if remaining == 0:
                return 1
            if idx == n:
                return 0
            
            curr = 0
            for i in range(idx, n):
                if coins[i]>remaining:
                    continue
                curr += dfs(i, remaining-coins[i])
            return curr
        return dfs(0, amount)