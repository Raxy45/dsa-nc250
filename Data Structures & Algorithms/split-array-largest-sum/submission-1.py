class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lowest_sum, highest_sum = max(nums), sum(nums)
        res = highest_sum

        def get_sub_arr_count(c_mid_sum):
            c_subarr_count = 1
            c_sum = 0
            for i in nums:
                c_sum += i
                if c_sum<=c_mid_sum:
                    continue
                else:
                    c_subarr_count += 1
                    c_sum = i
            return c_subarr_count

        while lowest_sum<=highest_sum:
            mid_sum = (lowest_sum+highest_sum)//2
            subarr_count = get_sub_arr_count(mid_sum)
            print('for sum ', mid_sum, 'count is ', subarr_count)
            if subarr_count <= k:
                highest_sum = mid_sum-1
            else:
                lowest_sum = mid_sum+1
            
            print('high sum', highest_sum)
            print('loest sum', lowest_sum)
        return lowest_sum