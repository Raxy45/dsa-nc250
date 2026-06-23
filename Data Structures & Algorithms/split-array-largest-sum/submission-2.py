class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, h = max(nums), sum(nums)

        def get_sub_count(curr_max):
            count = 0
            curr_sum = 0
            for i in nums:
                curr_sum += i
                if curr_sum==curr_max:
                    count += 1
                    curr_sum = 0
                elif curr_sum > curr_max:
                    count += 1
                    curr_sum = i
            
            if curr_sum > 0:
                count += 1
            return count
        
        ans = h
        while l<=h:
            m = (l+h)//2
            n_subs = get_sub_count(m)
            print(l, h)
            print('for m', m, 'n subs are', n_subs)
            if n_subs > k:
                l = m + 1
            else: 
                h = m - 1
                ans = min(ans, m)
        return ans