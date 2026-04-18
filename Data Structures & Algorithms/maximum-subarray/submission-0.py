class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr_sum= float('-inf'), 0
        for num in nums:
            curr_sum += num
            res = max(res, curr_sum)
            if curr_sum<0:
                curr_sum = 0
        return res