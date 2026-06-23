class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def solve(i):
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            if i == n:
                return 1
            
            cache[i] = solve(i+1) + solve(i+2)
            return cache[i]

        return solve(0)
        
