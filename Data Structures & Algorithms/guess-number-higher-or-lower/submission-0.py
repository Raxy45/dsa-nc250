# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ans = -1
        l = 1
        r = n
        while True:
            ans = (l+r)//2
            res = guess(ans)
            if res == 0:
                return ans
            elif res == -1:
                r = ans -1
            else:
                l = ans+1