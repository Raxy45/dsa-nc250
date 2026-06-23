class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        cache = defaultdict(int)
        def solve(till_now):
            nonlocal ans
            if till_now in cache:
                return cache[till_now]
            if till_now == n:
                return 1
            if till_now > n:
                return float('inf')
            
            t1 = solve(till_now+1)
            t2 = solve(till_now+2)
            cache[till_now+1] = t1 if t1!=float('inf') else 0
            cache[till_now+2] = t2 if t2!=float('inf') else 0
            print('returning',t1,t2, 'for', till_now)
            return cache[till_now+1] + cache[till_now+2]
        solve(0)
        return cache[1] + cache[2]