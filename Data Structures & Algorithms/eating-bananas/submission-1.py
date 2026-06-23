class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(k, piles):
            hours = 0
            for banana in piles:
                current = banana//k
                hours += current
                if banana%k > 0:
                    hours +=1
            
            if hours>h:
                return False
            return True
        low, high= 1, max(piles)
        ans = max(piles)
        while low<=high:
            mid = (low+high)//2
            if get_hours(mid, piles):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
