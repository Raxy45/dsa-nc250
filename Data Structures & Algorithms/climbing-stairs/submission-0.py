class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        def solve(till_now):
            nonlocal ans
            if till_now == n:
                ans += 1
                return
            if till_now > n:
                return
            
            till_now += 1
            solve(till_now)

            till_now += 1
            solve(till_now)
        solve(0)
        return ans