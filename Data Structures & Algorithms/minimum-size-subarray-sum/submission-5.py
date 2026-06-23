class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        min_sub = len(nums)+1
        c_sum = 0

        for r in range(0, len(nums)):
            c_sum += nums[r]

            while l<=r and c_sum >= target:
                min_sub = min(min_sub, r-l+1)
                c_sum -= nums[l]
                l += 1
        
        if min_sub == len(nums)+1: return 0
        return min_sub
        while r < len(nums):
            while r<len(nums) and c_sum < target:
                print('in first while sum < target')
                # print('current num: ', nums[r])
                c_sum += nums[r]
                # print('after adding r -> sum: ', c_sum)
                r += 1
            if r > len(nums):
                # print('r was above len of nums')
                break
            
            if c_sum >= target:
                # print('*'*30)
                # print('r. is ', r)
                # print('c_sum is gt than target')
                min_sub = r - l
                # print('c min sub: ', min_sub)
                # print('*'*30)
            while l<r and c_sum > target:
                c_sum -= nums[l]
                l += 1
                if c_sum >= target:
                    min_sub = r - l
        
        if min_sub == len(nums)+1:
            return 0
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