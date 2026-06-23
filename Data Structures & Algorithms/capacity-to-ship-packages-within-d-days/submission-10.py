class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)

        def get_days(w):
            curr_s, curr_d = 0, 0
            for i in weights:
                curr_s += i
                if curr_s < w:
                    continue
                if curr_s == w:
                    curr_s = 0
                if curr_s > w:
                    curr_s = i
                curr_d += 1
            
            if curr_s > 0:
                curr_d += 1
            return curr_d
        ans = h
        while l <=h :
            wt = (l+h)//2
            curr_days = get_days(wt)
            if curr_days <= days:
                ans = min(ans, wt)
                h = wt - 1
            else:
                l = wt + 1
        return ans