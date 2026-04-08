class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time Complexity: O(n * amount)
        # - Each state (idx, t) computed once

        # Space Complexity: O(n * amount) + O(amount)
        # - dp dictionary + recursion stack

        n = len(coins)
        dp = {}

        def solve(idx, t):
            if t == 0:
                return 1
            if idx == n:
                return 0

            if (idx, t) in dp:
                return dp[(idx, t)]

            # take coin[idx]
            take = 0
            if t >= coins[idx]:
                take = solve(idx, t - coins[idx])

            # skip coin[idx]
            skip = solve(idx + 1, t)

            dp[(idx, t)] = take + skip
            return dp[(idx, t)]

        return solve(0, amount)

class SolutionBottomUP2DDP:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time Complexity: O(n * amount)
        # - Filling dp table of size n x amount

        # Space Complexity: O(n * amount)
        # - Full dp table

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # base case: amount 0 → 1 way
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for t in range(1, amount + 1):
                # skip
                dp[i][t] = dp[i + 1][t]

                # take
                if t >= coins[i]:
                    dp[i][t] += dp[i][t - coins[i]]

        return dp[0][amount]

class Solution1DDP:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time Complexity: O(n * amount)
        # - Nested loops over coins and amounts

        # Space Complexity: O(amount)
        # - 1D dp array

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for t in range(coin, amount + 1):
                dp[t] += dp[t - coin]

        return dp[amount]