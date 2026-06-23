class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_b = 1
        high_b = max(piles)
        ans = high_b
        while low_b<=high_b:
            curr_b = (low_b+high_b)//2
            curr_hour = 0
            for i in piles:
                curr_hour += math.ceil(i/curr_b)
            
            if curr_hour <= h:
                ans = curr_b
                high_b = curr_b-1
            elif curr_hour > h:
                low_b = curr_b+1
            
        return ans
