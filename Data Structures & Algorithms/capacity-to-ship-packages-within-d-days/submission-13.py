class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days(wt):
            d = 0
            curr = 0
            # print('finding for', wt)
            for w in weights:
                curr += w
                # print(curr, w)
                if curr>wt:
                    curr = w
                    d += 1
                elif curr == wt:
                    curr = 0
                    d += 1
            if curr>0:
                d += 1
            # print('final d',d)
            return d

        l, r = max(weights), sum(weights)
        while l<=r:
            curr_wt = (l+r)//2
            req_days = get_days(curr_wt) 
            # print(req_days, curr_wt)
            if req_days > days:
                l = curr_wt + 1
            else:
                r = curr_wt - 1
            # print('***')
        return r+1