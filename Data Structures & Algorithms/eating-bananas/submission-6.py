class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hour(banana):
            curr = 0
            for p in piles:
                curr += (p//banana)

                if (p%banana) > 0:
                    curr += 1
            return curr
        l, r = 1, sum(piles)
        ans = 0
        while l<=r:
            m = (l+r)//2
            hours_req = get_hour(m)
            print(hours_req, m)
            if hours_req>h:
                l =  m + 1
            else:
                r = m - 1
        return l

        