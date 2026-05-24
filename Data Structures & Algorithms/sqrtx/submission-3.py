class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            m = (l+r)//2
            sq = m**2
            if sq ==x:
                return m
            
            if sq<x:
                l = m + 1
            else:
                r = m - 1
        return r