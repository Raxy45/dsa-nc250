class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = 1
        ans = []
        subset = []

        def solve(num, subset):
            if len(subset) == k:
                ans.append(subset.copy())
                return

            for i in range(num, n+1):
                subset.append(i)

                solve(i+1, subset)

                subset.pop()

        solve(num, [])
        return ans