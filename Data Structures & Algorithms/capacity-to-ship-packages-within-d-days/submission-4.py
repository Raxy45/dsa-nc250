class Solution:
    def get_days(self, weight_cpc):
        curr_days = 0
        curr_weight_cpc = (min_weight+max_weight)//2
        # print('curr_cpc', curr_weight_cpc)
        weight_sum = 0
        for i in weights:
            weight_sum += i
            if weight_sum > curr_weight_cpc:
                curr_days += 1
                weight_sum = i  # start new day with current package
            elif weight_sum == curr_weight_cpc:
                curr_days += 1
                weight_sum = 0  # exactly filled a day
        if weight_sum>0:
            curr_days += 1
        return curr_days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)
        # MIN

        ans = max_weight
        while min_weight<=max_weight:
            curr_weight_cpc = (min_weight+max_weight)//2
            curr_days = self.get_days(curr_weight_cpc)
            if curr_days>days:
                min_weight = curr_weight_cpc+1
            elif curr_days<=days:
                ans = min(ans, curr_weight_cpc)
                max_weight = curr_weight_cpc-1
            # print('*'*49)
        return ans