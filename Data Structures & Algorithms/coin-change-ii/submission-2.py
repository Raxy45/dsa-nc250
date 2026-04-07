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