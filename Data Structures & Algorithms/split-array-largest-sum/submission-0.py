class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lowest_sum, highest_sum = max(nums), sum(nums)
        res = highest_sum

        def get_sub_arr_count(c_mid_sum):
            c_subarr_count = 1
            c_sum = 0
            for i in nums:
                c_sum += i
                if c_sum<c_mid_sum:
                    continue
                else:
                    c_subarr_count += 1
                    c_sum = 1
            return c_subarr_count
            
        while low<=high:
            mid_sum = (low+high)//2
            subarr_count = get_sub_arr_count(mid_sum)
            if subarr_count < k:
                highest_sum = mid_sum-1
            elif subarr_count > k:
                lowest_sum = mid_sum+1
            else:
                res = mid_sum
                break
        return res