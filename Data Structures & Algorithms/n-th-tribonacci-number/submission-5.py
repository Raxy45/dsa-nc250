class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        t3 = None
        if n == 0: return t0
        if n == 1: return t1
        if n == 2: return t2
        for _ in range(3, n+1):
            t3 = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t3