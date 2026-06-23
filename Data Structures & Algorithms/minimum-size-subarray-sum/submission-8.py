class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i , curr_sum = 0, nums[0]
        if curr_sum>=target:
            return 1

        min_length = len(nums)+1
        for j in range(1,len(nums)):
            print('i', i)
            print('j', j)
            curr_sum += nums[j]
            while curr_sum>=target:
                print(curr_sum, nums[i], nums[j])
                min_length = min(min_length, j-i+1)
                curr_sum -= nums[i]
                i += 1
            
        if min_length == len(nums)+1: return 0
        return min_length

        i,j= 0,0
        min_len = len(nums)+1
        c_sum = 0
        for j in range(len(nums)):
            c_sum+=nums[j]
            while c_sum>=target:
                min_len=min(min_len, j-i+1)
                c_sum -= nums[i]
                i+=1
        if min_len>len(nums): return 0
        return min_len


        l = r = 0
        min_sub = len(nums)+1
        c_sum = 0

        for r in range(0, len(nums)):
            c_sum += nums[r]

            while c_sum >= target:
                min_sub = min(min_sub, r-l+1)
                c_sum -= nums[l]
                l += 1
        
        if min_sub == len(nums)+1: return 0
        return min_sub

        # brute
        ans_min = len(nums)+1
        for i in range(0, len(nums)):
            c_min = len(nums)+1
            c_sum = 0
            # print('i, j ', i)
            for j in range(i, len(nums)):
                c_sum += nums[j]
                # print('current sum: ', c_sum)
                if c_sum >= target:
                    c_min = j-i+1
                    break
            # print('current min: ', c_min)
            ans_min = min(ans_min, c_min)
        if ans_min == len(nums)+1:
            return 0
        return ans_min