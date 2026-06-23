class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days(w):
            req_days = 0
            w_sum = 0
            for current_w in weights:
                w_sum += current_w
                if w_sum>w:
                    req_days+=1
                    w_sum = current_w
                elif w_sum==w:
                    req_days+=1
                    w_sum = 0 
                else:
                    continue
            
            print('req days', req_days)
            if w_sum>0:
                req_days+=1
            if req_days>days:
                return False
            return True
        min_w, max_w = max(weights), sum(weights)
        ans = max_w

        print('min_w', min_w)
        print('max_w', max_w)
        while min_w<=max_w:
            current_w = (min_w + max_w)//2
            print('current_w', current_w)
            if get_days(current_w):
                ans = current_w
                max_w = current_w-1
            else:
                min_w = current_w+1
        return ans