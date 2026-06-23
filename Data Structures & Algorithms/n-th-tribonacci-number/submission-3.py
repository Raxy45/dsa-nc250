class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n <=2: return 1
        for i in range(2, n):
            curr = t0+t1+t2
            t0, t1, t2 = t1, t2, curr
        return curr