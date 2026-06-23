class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        t3 = None
        for _ in range(3, n+1):
            t3 = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t3