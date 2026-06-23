class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
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