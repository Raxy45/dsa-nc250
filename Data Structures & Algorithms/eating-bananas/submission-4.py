class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        def get_hours(h):
            req = 0
            for banana in piles:
                req += banana//h
                if (banana % h) > 0:
                    req += 1
            return req
        while l<=r:
            print(l, r)
            mid = (l+r)//2
            hours_req = get_hours(mid)
            print('hours for', mid,'are', hours_req, h, hours_req<h)
            if hours_req <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans