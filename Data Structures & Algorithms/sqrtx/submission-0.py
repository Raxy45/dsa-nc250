class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l<=r:
            mid = (l+r)//2
            curr_ans = mid*mid
            print(l, r, mid)
            print(curr_ans)
            if curr_ans==x:
                return mid
            elif curr_ans<x:
                print('l is mid')
                l = mid+1
            else:
                r= mid-1
        return r