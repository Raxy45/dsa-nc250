class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 0
        def solve(r, c):
            nonlocal ans
            if r == m or c==n or min(r,c) < 0:
                return 0
            if r==m-1 and c==n-1:
                ans += 1
            
            solve(r+1, c)
            solve(r, c+1)
        solve(0, 0)
        return ans