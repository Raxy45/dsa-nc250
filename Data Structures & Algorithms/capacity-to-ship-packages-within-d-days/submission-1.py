class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)
        # MIN

        ans = max_weight
        while min_weight<=max_weight:
            # print('min cpc, max cpc', min_weight, max_weight)
            curr_days = 0
            curr_weight_cpc = (min_weight+max_weight)//2
            # print('curr_cpc', curr_weight_cpc)
            weight_sum = 0
            for i in weights:
                # print('i ', i)
                weight_sum += i

                # print('weight sum before ', weight_sum)
                if weight_sum<curr_weight_cpc:
                    pass
                elif weight_sum>curr_weight_cpc:
                    curr_days += 1
                    weight_sum = i
                else:
                    curr_days += 1
                    weight_sum = 0
                    # print('refreshed')
            if weight_sum>0:
                curr_days += 1
                # print('weight sum post ', weight_sum)
                # print('curr_days ', curr_days)
            # print('curr_sum oustide is ', weight_sum)
            # print('for weight ', curr_weight_cpc, ' days are ', curr_days)
            if curr_days>days:
                min_weight = curr_weight_cpc+1
            elif curr_days<=days:
                ans = min(ans, curr_weight_cpc)
                max_weight = curr_weight_cpc-1
            # print('*'*49)
        return ans